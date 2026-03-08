class UsageRecord:
    def __init__(self, section, question_id, question_text, response_code, response, group, count):
        self.section = section
        self.question_id = str(question_id)
        self.question_text = question_text
        self.response_code = int(response_code)
        self.response = response
        self.group = group
        self.count = int(count)

    def is_year_in_school(self) -> bool:
        return self.question_id == "72"
    def class_level(self):
        if not self.is_year_in_school():
            return None

        under = {"1st year undergraduate",
                 "2nd year undergraduate"}
        upper = {"3rd year undergraduate",
                 "4th year undergraduate",
                 "5th year or more undergraduate"}

        if self.response in under:
            return "Underclassmen"
        if self.response in upper:
            return "Upperclassmen"
        return "Other"

    def __repr__(self):
        return f"UsageRecord(qid={self.question_id}, response={self.response}, group={self.group}, count={self.count})"