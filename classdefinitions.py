class UsageRecord:
    def __init__(self, section, question_id, substance, response, group, count):
        self.section = section
        self.question_id = str(question_id)   # keep it consistent (strings)
        self.substance = substance
        self.response = response
        self.group = group
        self.count = int(count)

    def is_year_in_school(self) -> bool:
        return self.question_id == "72"

    def class_level(self):
        if not self.is_year_in_school():
            return None

        underclassmen = {
            "1st year undergraduate",
            "2nd year undergraduate",
        }
        upperclassmen = {
            "3rd year undergraduate",
            "4th year undergraduate",
            "5th year or more undergraduate",
        }

        if self.response in underclassmen:
            return "Underclassmen"
        if self.response in upperclassmen:
            return "Upperclassmen"
        return "Other"

    def __repr__(self):
        return (
            f"UsageRecord(section={self.section!r}, question_id={self.question_id!r}, "
            f"response={self.response!r}, group={self.group!r}, count={self.count})"
        )