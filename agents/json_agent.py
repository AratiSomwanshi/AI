# agents/json_agent.py
import json
from memory.mysql_memory import save_to_memory

REQUIRED_FIELDS = ["invoice_id", "customer", "items", "total"]

def handle_json(json_content):
    print("📦 JSON Agent Activated")

    try:
        data = json.loads(json_content)
    except json.JSONDecodeError as e:
        print(f"❌ JSON decode error: {e}")
        return

    missing_fields = [field for field in REQUIRED_FIELDS if field not in data]

    if missing_fields:
        result = {
            "status": "error",
            "missing_fields": missing_fields
        }
    else:
        result = {
            "status": "ok",
            "invoice_id": data["invoice_id"],
            "customer": data["customer"],
            "total": data["total"],
            "item_count": len(data["items"])
        }

    print("Extracted JSON Info:")
    print(result)

    save_to_memory("JSONAgent", "JSON", "Invoice", str(result))
