from dataset.dictionary import data

SLEEP_HOURS = {
    "Less than 4 hours": 3.0,
    "4-5 hours": 4.5,
    "6-7 hours": 6.5,
    "8+ hours": 8.0,
}
SLEEP_HOURS.update({
    "4–5 hours": 4.5,
    "6–7 hours": 6.5,
})

def avg_sleep_hours(dataset, qid: str, group: str = "Total") -> float:
    total = 0
    weighted_sum = 0.0

    for r in dataset.by_qid_and_group(qid, group):
        hours = SLEEP_HOURS.get(r.response)
        if hours is None:
            continue

        total += r.count
        weighted_sum += hours * r.count

    if total == 0:
        return 0.0

    return weighted_sum / total

