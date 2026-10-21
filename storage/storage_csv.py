# storage_csv.py

import csv
import os
import time

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
LOG_FILE = os.path.join(DATA_DIR, "logs.csv")


def log(message):
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, mode="a", newline="", encoding="utf-8") as file:
        fieldnames = ["Time", "Message"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(
            {"Time": time.asctime(time.localtime(time.time())), "Message": message}
        )
