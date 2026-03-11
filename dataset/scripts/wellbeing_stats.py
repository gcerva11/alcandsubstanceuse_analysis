from dataset.dictionary import data

frequency = {
    "Never": 0,
    "Once or twice": 1,
    "Monthly": 2,
    "Weekly": 3,
    "Daily or almost daily": 4,
}

def sleep_habits(qid: str, group: str = "Total") -> float:
    q = data.get(qid, {})
    responses = q.get("responses", {})

    weighted_sum = 0
    total_count = 0

    for info in responses.values():
        label = info.get("response", "")
        count = info.get("counts", {}).get(group, 0)

        score = frequency.get(label)
        if score is None:
            continue

        weighted_sum += score * count
        total_count += count

    if total_count == 0:
        return 0.0

    return weighted_sum / total_count