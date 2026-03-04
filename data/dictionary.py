import csv
import os

data = {}

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "master_data.csv")

with open(file_path, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)

    for row in reader:
        # Skip bad or incomplete rows
        if len(row) < 7 or row[3].strip() == "" or row[6].strip() == "":
            continue

        section = row[0]
        qid = row[1]
        question_text = row[2]
        response_code = int(row[3])
        response = row[4]
        gender = row[5]
        count = int(row[6])

        if qid not in data:
            data[qid] = {
                "section": section,
                "question_text": question_text,
                "responses": {}
            }

        if response_code not in data[qid]["responses"]:
            data[qid]["responses"][response_code] = {
                "response": response,
                "counts": {}
            }

        data[qid]["responses"][response_code]["counts"][gender] = count