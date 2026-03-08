#We want to find the average drinking and drug use within participants who identified as male, female and transgender/non-conforming.
#This document is for alcohol and that don't classify as drugs and other entities.

frequency = {
    "Never":0,
    "Once or twice":1,
    "Monthly":2,
    "Weekly": 3,
    "Daily or almost daily":4,
}

def avg_alcohol_usage(qid: str, group: str = "Total")-> float:
    question = data.get(qid)
    if not question:
        return 0.0
    responses = question.get("responses")

    weighted_sum = 0.0
    total_count = 0.0

    for information in reponses.value()
        label =  info.get("response", "")
        count = info.get("count", {}).get(group, 0)

        score = frequency.get(label)
        if score is None:
            continue

        weighted_sum += score * count
        total_count += count

    if total_count == 0.0:
        return 0.0

    return weighted_sum / total_count