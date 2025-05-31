# agents/classifier_agent.py
import os
import json
import fitz  # PyMuPDF
from memory.mysql_memory import save_to_memory
from agents.email_agent import handle_email
from agents.pdf_agent import handle_pdf
from agents.json_agent import handle_json

def detect_format(file_path):
    if file_path.endswith(".json"):
        return "JSON"
    elif file_path.endswith(".pdf"):
        return "PDF"
    elif file_path.endswith(".txt"):
        return "Email"
    else:
        return "Unknown"

def detect_intent(content):
    content_lower = content.lower()
    if "invoice" in content_lower:
        return "Invoice"
    elif "rfq" in content_lower or "quote" in content_lower:
        return "RFQ"
    elif "complaint" in content_lower or "issue" in content_lower:
        return "Complaint"
    elif "regulation" in content_lower or "policy" in content_lower:
        return "Regulation"
    else:
        return "Unknown"

def extract_pdf_text(file_path):
    try:
        doc = fitz.open(file_path)
        if doc.page_count == 0:
            print(f"⚠️ PDF '{file_path}' has no pages.")
            return ""
        text = ""
        for page in doc:
            text += page.get_text()
        return text.strip()
    except Exception as e:
        print(f"❌ Error opening or reading PDF '{file_path}': {e}")
        return ""

def classify_and_route(file_path):
    format_type = detect_format(file_path)

    if format_type == "Unknown":
        print("❌ Unsupported file format.")
        return

    if format_type == "PDF":
        content = extract_pdf_text(file_path)
        if not content:
            print(f"⚠️ Skipping unreadable PDF: {file_path}")
            return
    else:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"❌ Failed to read file '{file_path}': {e}")
            return

    intent = detect_intent(content)
    save_to_memory(file_path, format_type, intent, content[:500])

    if format_type == "JSON":
        handle_json(content)
    elif format_type == "Email":
        handle_email(content)
    elif format_type == "PDF":
        handle_pdf(content)
