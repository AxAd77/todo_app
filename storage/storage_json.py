# storage_json.py

import json
import os
import time

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
LOG_FILE = os.path.join(DATA_DIR, "logs.json")


def log(message):
    log_entry = {"Time": time.asctime(time.localtime(time.time())), "Message": message}

    if os.path.isfile(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
    else:
        data = []

    data.append(log_entry)

    with open(LOG_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
