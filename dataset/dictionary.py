import csv
import os

# Global dictionary that stores everything
data = {}

# Find master_data.csv in the same folder as this file
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "master_data.csv")

with open(file_path, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)

    # Skip header row (safe even if no header)
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

        # response_code and count should be numbers
        try:
            response_code = int(row[3])
            count = int(row[6])
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
        if response_code not in data[qid].get("responses", {}):
            data[qid]["responses"][response_code] = {
                "response": response,
                "counts": {}
            }

        # Store count under the group
        data[qid]["responses"][response_code]["counts"][group] = count


# -----------------------------
# Helper Functions (CSC101 style)
# -----------------------------

def get_question(qid: str) -> dict:
    """Return the dictionary for a question id, or {} if not found."""
    return data.get(str(qid), {})


def get_responses(qid: str) -> dict:
    """Return the responses dictionary for a question id, or {} if not found."""
    question = get_question(qid)
    return question.get("responses", {})


def get_count(qid: str, response_code: int, group: str = "Total") -> int:
    """Return the count for a specific response_code and group, or 0 if missing."""
    responses = get_responses(qid)
    info = responses.get(response_code, {})
    counts = info.get("counts", {})
    return counts.get(group, 0)


def groups_for_question(qid: str) -> list:
    """
    Return a list of group names that appear for this question.
    Example: ["Cis Men", "Cis Women", "TGNC", "Total"]
    """
    responses = get_responses(qid)
    group_set = set()

    for info in responses.values():
        counts = info.get("counts", {})
        for g in counts.keys():
            group_set.add(g)

    return sorted(list(group_set))