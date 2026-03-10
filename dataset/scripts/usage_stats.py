#We want to find the average drinking and drug use within participants who identified as male, female and transgender/non-conforming.
#This document is for alcohol and that don't classify as drugs and other entities.

from dataset.dictionary import data

FREQUENCY_SCORE = {
    "Never": 0,
    "Once or twice": 1,
    "Monthly": 2,
    "Weekly": 3,
    "Daily or almost daily": 4,
}

def average_frequency_score(dataset, qid, group="Total"):
    records = dataset.by_qid_and_group(qid, group)

    weighted_sum = 0
    total_count = 0

    for r in records:
        score = FREQUENCY_SCORE.get(r.response, None)
        if score is None:
            continue

        weighted_sum += score * r.count
        total_count += r.count

    if total_count == 0:
        return 0.0

    return weighted_sum / total_count