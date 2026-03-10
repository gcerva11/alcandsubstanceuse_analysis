import csv
import os
from classdefinitions import UsageRecord

records = []

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "master_data_cleaned.csv")

with open(file_path, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader, None)

    for row in reader:
        if len(row) < 7:
            continue

        record = UsageRecord(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6]
        )

        records.append(record)