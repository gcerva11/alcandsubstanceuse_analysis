from dataset.dictionary import data

def sleep_hours_value(response: str) -> float | None:
    s = (response or "").strip()

    if s == "Less than 4 hours":
        return 3.0

    if s == "10 or more hours":
        return 10.0

    # Handles: "4 hours", "5 hours", "6 hours", "7 hours", "8 hours", "9 hours"
    if s.endswith(" hours"):
        first = s.split()[0]  # "4" from "4 hours"
        if first.isdigit():
            return float(first)

    return None


def avg_sleep_hours(dataset, qid: str, group: str = "Total") -> float:
    total = 0
    weighted_sum = 0.0

    for r in dataset.by_qid_and_group(qid, group):
        hours = sleep_hours_value(r.response)
        if hours is None:
            continue

        total += r.count
        weighted_sum += hours * r.count

    return (weighted_sum / total) if total else 0.0