from dataset.dictionary import data

GRADE_POINTS = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D+": 1.3, "D": 1.0, "D-": 0.7,
    "F": 0.0,
}

def normalize_grade(label: str) -> str:
    """
    Fix messy labels like:
    'D- 6 0 15 0'
    'F 9 0 1'

    Returns just the grade part (e.g., 'D-' or 'F')
    """
    if not label:
        return ""

    return label.strip().split()[0]


def average_gpa(dataset, qid: str = "80", group: str = "Total") -> float:
    records = dataset.by_qid_and_group(qid, group)

    weighted_sum = 0.0
    total_count = 0

    for r in records:
        clean_grade = normalize_grade(r.response)
        points = GRADE_POINTS.get(clean_grade)

        if points is None:
            continue

        weighted_sum += points * r.count
        total_count += r.count

    if total_count == 0:
        return 0.0

    return weighted_sum / total_count