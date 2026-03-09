from dataset.dictionary import data
#Our goal is to be able to process stats regarding mental wellbeing with students (don't know what we want yet?)

#I think we should analyze sleeping habits and maybe mood if theres something there for that yaaaas

frequency = {
    "Never":0,
    "Once or twice":1,
    "Monthly":2,
    "Weekly": 3,
    "Daily or almost daily":4,
}

def sleep_habits(qid: str, group: str = "Total") -> float:
    question = data.get(qid)
    if not question:
        return 0.0
    responses = question.get("responses")

    weighted_sum = 0
    total_count = 0

    for information in responses.values():
        label =  info.get("response", "")
        count = info.get("count", {}).get(group, 0)

        score = frequency.get(label)
        if score is None:
            continue