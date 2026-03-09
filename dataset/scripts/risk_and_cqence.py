from dataset.dictionary import data
def high_risk_percent(qid: str, group: str = "Total") -> float:
    q = data.get(qid, {})
    responses = q.get("responses", {})

    high_risk_total = 0
    total = 0

    for info in responses.values():
        label = info.get("response", "")
        count = info.get("counts", {}).get(group, 0)

        total += count

        if label in ["Weekly", "Daily or almost daily"]:
            high_risk_total += count

    if total == 0:
        return 0.0

    return (high_risk_total / total) * 100

def consequence_percent(qid: str, group: str = "Total") -> float:
    q = data.get(qid, {})
    responses = q.get("responses", {})

    consequence_total = 0
    total = 0

    for info in responses.values():
        label = info.get("response", "")
        count = info.get("counts", {}).get(group, 0)

        total += count

        # Any response other than "Never" counts as a consequence
        if label != "Never":
            consequence_total += count

    if total == 0:
        return 0.0

    return (consequence_total / total) * 100