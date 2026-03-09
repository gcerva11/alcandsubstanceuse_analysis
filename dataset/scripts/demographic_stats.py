from dataset.dictionary import data
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