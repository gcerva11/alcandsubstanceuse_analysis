import csv
import os


data = {}

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "master_data.csv")

with open(file_path, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)

    # Skip header row if your CSV has one
    next(reader, None)

    for row in reader:
        # Skip incomplete rows
        if len(row) < 7 or row[3].strip() == "" or row[6].strip() == "":
            continue

        section = row[0]
        qid = row[1]
        question_text = row[2]
        response_code = int(row[3])
        response = row[4].strip()
        group = row[5].strip()
        count = int(row[6])

        # Create question level
        if qid not in data:
            data[qid] = {
                "section": section,
                "question_text": question_text,
                "responses": {}
            }

        # Create response level
        if response_code not in data[qid]["responses"]:
            data[qid]["responses"][response_code] = {
                "response": response,
                "counts": {}
            }

        # Store count by group
        data[qid]["responses"][response_code]["counts"][group] = count


#*************
# Helper Functions
#*************

def classify_year(response_label):
    """Classify a year label into Underclassmen or Upperclassmen."""
    under = {
        "1st year undergraduate",
        "2nd year undergraduate",
    }

    upper = {
        "3rd year undergraduate",
        "4th year undergraduate",
        "5th year or more undergraduate",
    }

    if response_label in under:
        return "Underclassmen"
    if response_label in upper:
        return "Upperclassmen"
    return "Other"


def upper_under_percentages(qid="72", group="Total"):
    """
    Calculate Underclassmen and Upperclassmen percentages
    for a given group (default = Total).
    """
    under_total = 0
    upper_total = 0

    if qid not in data:
        return 0.0, 0.0

    for response_code, info in data[qid]["responses"].items():
        label = info["response"]
        level = classify_year(label)
        count = info["counts"].get(group, 0)

        if level == "Underclassmen":
            under_total += count
        elif level == "Upperclassmen":
            upper_total += count

    total = under_total + upper_total

    if total == 0:
        return 0.0, 0.0

    return (under_total / total) * 100, (upper_total / total) * 100