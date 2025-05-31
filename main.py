# main.py
import os
from agents.classifier_agent import classify_and_route

DATA_FOLDER = "data"

for filename in os.listdir(DATA_FOLDER):
    file_path = os.path.join(DATA_FOLDER, filename)
    if os.path.isfile(file_path):
        print(f"\nProcessing file: {file_path}")
        classify_and_route(file_path)
