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


def upper_under_percentages(dataset, qid: str = "72", group: str = "Total") -> dict:
    under_total = 0
    upper_total = 0
    total = 0

    under_labels = {
        "1st year undergraduate",
        "2nd year undergraduate",
    }

    upper_labels = {
        "3rd year undergraduate",
        "4th year undergraduate",
        "5th year or more undergraduate",
    }

    # Pull records from the dataset
    for r in dataset.by_qid_and_group(qid, group):
        label = (r.response or "").strip()
        count = r.count

        total += count

        if label in under_labels:
            under_total += count
        elif label in upper_labels:
            upper_total += count

    if total == 0:
        return {"Underclassmen": 0.0, "Upperclassmen": 0.0}

    return {
        "Underclassmen": (under_total / total) * 100,
        "Upperclassmen": (upper_total / total) * 100,
    }