from dataset.dictionary import data

def classify_year(response_label: str) -> str:
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


def upper_under_percentages(data: dict, qid: str = "72", group: str = "Total") -> dict:
    q = data.get(str(qid), {})
    responses = q.get("responses", {})

    under_total = 0
    upper_total = 0
    total = 0

    for info in responses.values():
        label = info.get("response", "")
        count = info.get("counts", {}).get(group, 0)

        total += count

        level = classify_year(label)
        if level == "Underclassmen":
            under_total += count
        elif level == "Upperclassmen":
            upper_total += count

    if total == 0:
        return {"Underclassmen": 0.0, "Upperclassmen": 0.0}

    return {
        "Underclassmen": (under_total / total) * 100,
        "Upperclassmen": (upper_total / total) * 100
    }