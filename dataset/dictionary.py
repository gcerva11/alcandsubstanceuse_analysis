import csv
import os

data = {}

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "master_data.csv")

with open(file_path, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)

    # Skip header row
    next(reader, None)
    # Skip incomplete rows
    for row in reader:
        if len(row) < 7 or row[3].strip() == "" or row[6].strip() == "":
            continue

        section = row[0].strip()
        qid = row[1].strip()
        question_text = row[2].strip()
        response_code = int(row[3])
        response = row[4].strip()
        group = row[5].strip()
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

        data[qid]["responses"][response_code]["counts"][group] = count

def get_question(qid: str):
    return data.get(str(qid), {})

def response_items(qid: str):
    q = get_question(qid)
    responses = q.get("responses", {})
    return responses.items()

def get_count(qid: str, response_code: int, group: str = "Total") -> int:
    q = get_question(qid)
    responses = q.get("responses", {})
    info = responses.get(response_code, {})
    counts = info.get("counts", {})
    return counts.get(group, 0)