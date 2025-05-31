# 🤖 Multi-Agent AI Document Processing System

This project implements a **Multi-Agent AI System** capable of automatically processing and classifying documents of various types — Emails (`.txt`), Invoices (`.json`), and PDFs (`.pdf`). It uses intelligent agents to extract relevant information and store it in a shared MySQL memory.

---

## 📌 Features

- 📨 **Email Agent**: Extracts sender, urgency, and message snippet.
- 📦 **JSON Agent**: Extracts invoice data (customer, total, items).
- 📄 **PDF Agent**: Reads and classifies content from PDF files.
- 🧠 **Classifier Agent**: Detects file format and routes to appropriate agent.
- 🗄️ **Shared Memory (MySQL)**: Stores structured data with duplicate detection.

---

---

## 🛠️ Prerequisites

- ✅ Python 3.10+
- ✅ MySQL server installed and running
- ✅ Required Python packages:

```bash
pip install mysql-connector-python pymupdf

## MySQL Setup
CREATE DATABASE IF NOT EXISTS agent_memory_db;

USE agent_memory_db;

CREATE TABLE IF NOT EXISTS shared_memory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    source VARCHAR(255),
    format_type VARCHAR(50),
    intent VARCHAR(100),
    extracted_data TEXT
);
## 🚀 How to Run
python main.py

