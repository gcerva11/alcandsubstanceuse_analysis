from dataset.dictionary import data
#done by lupe
def community_harm_percent(dataset, qid: str, group: str = "Total") -> float:
    total = 0
    harm = 0

    for r in dataset.by_qid_and_group(qid, group):
        total += r.count
        if r.response.strip().lower() != "never":
            harm += r.count

    if total == 0:
        return 0.0

    return (harm / total) * 100


def academic_impact_ratio(dataset, usage_qid: str, academic_qid: str, group: str = "Total") -> float:
    high_risk_percent = dataset.high_risk_percent(usage_qid, group)

    total = 0
    harmed = 0

    for r in dataset.by_qid_and_group(academic_qid, group):
        total += r.count
        response_lower = r.response.lower()

        if "negatively" in response_lower or "delayed" in response_lower:
            harmed += r.count

    if total == 0 or high_risk_percent == 0:
        return 0.0

    academic_percent = (harmed / total) * 100

    return academic_percent / high_risk_percent


def disparity_index(value_dict: dict) -> float:

    if not value_dict:
        return 0.0

    values = list(value_dict.values())
    return max(values) - min(values)