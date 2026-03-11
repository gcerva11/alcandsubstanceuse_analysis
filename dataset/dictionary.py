import csv
import os
from classdefinitions import UsageRecord, Dataset
#dictionary made with the help of chatgpt to fix errors i couldnt figure out
# Global dictionary that stores everything
data = {}

# Find master_data_cleaned.csv in the same folder as this file
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "master_data_cleaned.csv")

with open(file_path, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)

    # Skip header row
    next(reader, None)

    for row in reader:
        # Skip incomplete rows
        if len(row) < 7:
            continue

        # Skip rows missing response_code or count
        if row[3].strip() == "" or row[6].strip() == "":
            continue

        section = row[0].strip()
        qid = row[1].strip()
        question_text = row[2].strip()

        # ResponseID might be "1.0" so parse as float first
        try:
            response_code = int(float(row[3].strip()))
            count = int(float(row[6].strip()))
        except ValueError:
            continue

        response = row[4].strip()
        group = row[5].strip()

        # Create the question-level dictionary if missing
        if qid not in data:
            data[qid] = {
                "section": section,
                "question_text": question_text,
                "responses": {}
            }

        # Create the response-level dictionary if missing
        if response_code not in data[qid]["responses"]:
            data[qid]["responses"][response_code] = {
                "response": response,
                "counts": {}
            }

        # Store count under the group
        data[qid]["responses"][response_code]["counts"][group] = count

def build_dataset_from_data(data_dict: dict) -> Dataset:
    records = []

    for qid, qinfo in data_dict.items():
        section = qinfo.get("section", "")
        question_text = qinfo.get("question_text", "")
        responses = qinfo.get("responses", {})

        for response_code, rinfo in responses.items():
            response_label = rinfo.get("response", "")
            counts = rinfo.get("counts", {})

            for group, count in counts.items():
                records.append(
                    UsageRecord(
                        section=section,
                        question_id=qid,
                        question_text=question_text,
                        response_code=response_code,
                        response=response_label,
                        group=group,
                        count=count
                    )
                )

    return Dataset(records)

#helper functions made with no chatgpt
def get_question(qid: str) -> dict:
    return data.get(str(qid), {})


def get_responses(qid: str) -> dict:
    question = get_question(qid)
    return question.get("responses", {})


def get_count(qid: str, response_code: int, group: str = "Total") -> int:
    responses = get_responses(qid)
    info = responses.get(response_code, {})
    counts = info.get("counts", {})
    return counts.get(group, 0)


def groups_for_question(qid: str) -> list:
    responses = get_responses(qid)
    group_set = set()

    for info in responses.values():
        counts = info.get("counts", {})
        for g in counts.keys():
            group_set.add(g)

    return sorted(list(group_set))