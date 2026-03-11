import unittest
from classdefinitions import UsageRecord, Dataset


class TestClassDefinitions(unittest.TestCase):

    def test_usage_record_class_level_under(self):
        r = UsageRecord("Demographics", "72", "Year in school", 1, "1st year undergraduate", "Total", 100)
        self.assertEqual(r.class_level(), "Underclassmen")

    def test_usage_record_class_level_upper(self):
        r = UsageRecord("Demographics", "72", "Year in school", 3, "3rd year undergraduate", "Total", 100)
        self.assertEqual(r.class_level(), "Upperclassmen")

    def test_usage_record_class_level_other(self):
        r = UsageRecord("Demographics", "72", "Year in school", 9, "Other", "Total", 100)
        self.assertEqual(r.class_level(), "Other")

    def test_dataset_by_qid_and_group_filters(self):
        # Build UsageRecord objects directly (this matches how Dataset is designed)
        records = [
            UsageRecord("Demographics", "72", "What is your year in school?", 1, "1st year undergraduate", "Total", 10),
            UsageRecord("Demographics", "72", "What is your year in school?", 2, "2nd year undergraduate", "Total", 20),
            UsageRecord("Demographics", "72", "What is your year in school?", 1, "1st year undergraduate", "Cis Men", 3),
            UsageRecord("Demographics", "72", "What is your year in school?", 2, "2nd year undergraduate", "Cis Men", 7),
        ]

        dataset = Dataset(records)

        records_total = dataset.by_qid_and_group("72", "Total")

        self.assertEqual(len(records_total), 2)

        records_men = dataset.by_qid_and_group("72", "Cis Men")

        self.assertEqual(len(records_men), 2)
        self.assertEqual(records_men[0].count, 3)
        self.assertEqual(records_men[1].count, 7)

if __name__ == "__main__":
    unittest.main()