#We want to find the average drinking and drug use within participants who identified as male, female and transgender/non-conforming.
#This document is for alcohol and that don't classify as drugs and other entities.

from dataset.dictionary import data

frequency = {
    "Never": 0,
    "Once or twice": 1,
    "Monthly": 2,
    "Weekly": 3,
    "Daily or almost daily": 4,
}


def avg_alcohol_usage(qid: str, group: str = "Total") -> float:
    question = data.get(qid, {})
    responses = question.get("responses", {})

    weighted_sum = 0.0
    total_count = 0.0

    for info in responses.values():
        label = info.get("response", "")
        count = info.get("counts", {}).get(group, 0)

        score = frequency.get(label)
        if score is None:
            continue

        weighted_sum += score * count
        total_count += count

    if total_count == 0.0:
        return 0.0

    return weighted_sum / total_count


def avg_substance_usage(qid: str, group: str = "Total") -> float:
    question = data.get(qid, {})
    responses = question.get("responses", {})

    weighted_sum = 0.0
    total_count = 0.0

    for info in responses.values():
        label = info.get("response", "")
        count = info.get("counts", {}).get(group, 0)

        score = frequency.get(label)
        if score is None:
            continue

        weighted_sum += score * count
        total_count += count

    if total_count == 0.0:
        return 0.0

    return weighted_sum / total_count