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