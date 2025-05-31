# memory/mysql_memory.py
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="cdac",
        database="agent_memory_db"
    )

def save_to_memory(source, format_type, intent, extracted_data):
    conn = connect_db()
    try:
        # Step 1: Check for duplicates
        check_query = """
            SELECT id FROM shared_memory 
            WHERE source=%s AND format_type=%s AND intent=%s AND extracted_data=%s
        """
        with conn.cursor() as cursor:
            cursor.execute(check_query, (source, format_type, intent, extracted_data))
            result = cursor.fetchone()

        if result:
            print(f"⚠️ Duplicate found (id={result[0]}), skipping insert.")
        else:
            # Step 2: Insert if not duplicate
            insert_query = """
                INSERT INTO shared_memory (source, format_type, intent, extracted_data)
                VALUES (%s, %s, %s, %s)
            """
            with conn.cursor() as cursor:
                cursor.execute(insert_query, (source, format_type, intent, extracted_data))
            conn.commit()
            print("✅ Saved to shared_memory")
    finally:
        conn.close()
