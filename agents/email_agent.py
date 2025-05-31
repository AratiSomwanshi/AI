import re
from memory.mysql_memory import save_to_memory

def extract_sender(content):
    # Try to extract sender email or company name from signature
    match = re.search(r"Thanks,\s*\n(.*)", content, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return "Unknown Sender"

def detect_urgency(content):
    urgency_keywords = ["urgent", "as soon as possible", "immediately", "priority"]
    for word in urgency_keywords:
        if word in content.lower():
            return "High"
    return "Normal"

def handle_email(content):
    print("📨 Email Agent Activated")

    sender = extract_sender(content)
    urgency = detect_urgency(content)

    extracted_info = {
        "sender": sender,
        "urgency": urgency,
        "content_snippet": content[:300]
    }

    print("Extracted Email Info:")
    print(extracted_info)

    # Save extracted info to shared memory
    save_to_memory(source="EmailAgent", format_type="Email", intent="RFQ", extracted_data=str(extracted_info))
