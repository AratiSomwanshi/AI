from memory.mysql_memory import save_to_memory
import re

def extract_invoice_number(content):
    # Look for something like "Invoice #: INV-12345"
    match = re.search(r"invoice\s*#?:?\s*([A-Za-z0-9\-]+)", content, re.IGNORECASE)
    return match.group(1) if match else None

def extract_date(content):
    # Look for dates in simple formats (MM/DD/YYYY or YYYY-MM-DD)
    match = re.search(r"(\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2})", content)
    return match.group(1) if match else None

def handle_pdf(content):
    print("📄 PDF Agent Activated")

    invoice_number = extract_invoice_number(content)
    invoice_date = extract_date(content)

    missing_fields = []
    if not invoice_number:
        missing_fields.append("invoice_number")
    if not invoice_date:
        missing_fields.append("invoice_date")

    if missing_fields:
        result = {
            "status": "error",
            "missing_fields": missing_fields
        }
    else:
        result = {
            "status": "ok",
            "invoice_number": invoice_number,
            "invoice_date": invoice_date
        }

    print("Extracted PDF Info:")
    print(result)

    # ✅ Save to MySQL (duplicate-safe)
    save_to_memory(
        source="PDFAgent",
        format_type="PDF",
        intent="Invoice",
        extracted_data=str(result)
    )
