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
        qid = row[1].strip()
        question_text = row[2].strip()
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

#this function makes sure we can get the diction without the program crashing
def question(qid:str)-> str:
    return data.get(str(qid), {})

#this one is going to loop the response in order to get the information for specifc questions
def responces_loop(qid:str)-> str:
    question = question(qid)
    responces = question.get("responces", {})
    return responces.items() #should return like (responce #, informaton)

#this one is going to get a count
def getcount(qid, response_code, group="total")


def classify_year(response_label:str) -> str:
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

#calculates upper and underclassmen percentages (and totals)
#core alaysis function
def upper_under_percentages(qid: str = "72", group: str = "Total") -> dict[str, float]:
    under_total = 0
    upper_total = 0
    total = 0

    q = data.get(qid)
    if not q:
        return {"Underclassmen": 0.0, "Upperclassmen": 0.0}

    for info in q.get("responses", {}).values():
        label = info.get("response")
        count = info.get("counts", {}).get(group, 0)

        total += count

        if label in ["1st year undergraduate", "2nd year undergraduate"]:
            under_total += count
        elif label in [
            "3rd year undergraduate",
            "4th year undergraduate",
            "5th year or more undergraduate"
        ]:
            upper_total += count

    if total == 0:
        return {"Underclassmen": 0.0, "Upperclassmen": 0.0}

    return {
        "Underclassmen": (under_total / total) * 100,
        "Upperclassmen": (upper_total / total) * 100
    }

#calculates the high risk percentages per group
#also a core analysis function
def high_risk_percent(qid: str, group: str ="Total")-> float:
    q = data.get(qid)
    if not q:
        return 0.0

    high_risk_total = 0
    total = 0

    responses = q.get("responses", {})

    for info in responses.values():
        label = info.get("response")
        counts = info.get("counts", {})
        count = counts.get(group, 0)

        total += count

        if label in ["Weekly", "Daily or almost daily"]:
            high_risk_total += count

    if total == 0:
        return 0.0

    return (high_risk_total / total) * 100
#need a function to calculate gpa per group

#think it would be cool to analyze substance type per group too if we have time :)

#consequences
def consequence_percentage(qid: str, group: str = "Total")->float:
    consequence = 0
    total = 0

    response = responses(qid)
    if not response:
        return 0.0

    for information in response:
        label = information.get("response", "")
        count = (info, group)

        total += count
        if label != "Never"
            consequence += count
        if total = 0:
            return 0.0
    return (consequence / total)*100