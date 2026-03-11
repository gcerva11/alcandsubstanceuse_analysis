class UsageRecord:
    def __init__(self, section, question_id, question_text, response_code, response, group, count):
        self.section = section
        self.question_id = str(question_id)
        self.question_text = question_text
        self.response_code = int(response_code)
        self.response = response
        self.group = group
        self.count = int(count)

    def is_year_in_school(self):
        return self.question_id == "72"

    def class_level(self):
        if not self.is_year_in_school():
            return None

        under = {
            "1st year undergraduate",
            "2nd year undergraduate"
        }
        upper = {
            "3rd year undergraduate",
            "4th year undergraduate",
            "5th year or more undergraduate"
        }

        if self.response in under:
            return "Underclassmen"
        if self.response in upper:
            return "Upperclassmen"
        return "Other"

    def __repr__(self):
        return f"UsageRecord(qid={self.question_id}, response={self.response}, group={self.group}, count={self.count})"


class Dataset:
    def __init__(self, records):
        self.records = records

    def by_qid(self, qid: str):
        return [r for r in self.records if r.question_id == str(qid)]

    def by_qid_and_group(self, qid: str, group: str):
        return [r for r in self.by_qid(qid) if r.group == group]

    def underclass_percent(self, group: str = "Total") -> float:
        under = 0
        upper = 0

        for r in self.by_qid_and_group("72", group):
            level = r.class_level()
            if level == "Underclassmen":
                under += r.count
            elif level == "Upperclassmen":
                upper += r.count

        total = under + upper
        if total == 0:
            return 0.0

        return (under / total) * 100

    def upperclass_percent(self, group: str = "Total") -> float:
        under = 0
        upper = 0

        for r in self.by_qid_and_group("72", group):
            level = r.class_level()
            if level == "Underclassmen":
                under += r.count
            elif level == "Upperclassmen":
                upper += r.count

        total = under + upper
        if total == 0:
            return 0.0

        return (upper / total) * 100

    def high_risk_percent(self, qid: str, group: str = "Total") -> float:
        high = 0
        total = 0

        for r in self.by_qid_and_group(qid, group):
            total += r.count
            if r.response in ["Weekly", "Daily or almost daily"]:
                high += r.count

        if total == 0:
            return 0.0

        return (high / total) * 100

    def consequence_percent(self, qid: str, group: str = "Total") -> float:
        consequence = 0
        total = 0

        for r in self.by_qid_and_group(qid, group):
            total += r.count
            if r.response != "Never":
                consequence += r.count

        if total == 0:
            return 0.0

        return (consequence / total) * 100