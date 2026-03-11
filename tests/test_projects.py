import unittest

from classdefinitions import UsageRecord, Dataset
from dataset.scripts.usage_stats import average_frequency_score
from dataset.scripts.demographic_stats import classify_year
from dataset.scripts.academic_stats import average_gpa

def make_record(qid: str, response: str, group: str, count: int):
    return UsageRecord(
        section="TestSection",
        question_id=qid,
        question_text="Test Question",
        response_code=1,
        response=response,
        group=group,
        count=count
    )

class TestUsageRecord(unittest.TestCase):

    def test_is_year_in_school_true(self):
        r = make_record("72", "1st year undergraduate", "Total", 10)
        self.assertTrue(r.is_year_in_school())

    def test_is_year_in_school_false(self):
        r = make_record("80", "A", "Total", 10)
        self.assertFalse(r.is_year_in_school())

    def test_class_level_under(self):
        r = make_record("72", "1st year undergraduate", "Total", 10)
        self.assertEqual(r.class_level(), "Underclassmen")

    def test_class_level_upper(self):
        r = make_record("72", "4th year undergraduate", "Total", 10)
        self.assertEqual(r.class_level(), "Upperclassmen")

    def test_class_level_other(self):
        r = make_record("72", "Master's (MA, MS, etc.)", "Total", 10)
        self.assertEqual(r.class_level(), "Other")

class TestDataset(unittest.TestCase):

    def setUp(self):
        self.records = [
            make_record("72", "1st year undergraduate", "Total", 50),
            make_record("72", "2nd year undergraduate", "Total", 50),
            make_record("72", "3rd year undergraduate", "Total", 100),

            make_record("22B12", "Weekly", "Total", 10),
            make_record("22B12", "Daily or almost daily", "Total", 5),
            make_record("22B12", "Monthly", "Total", 5),
        ]

        self.dataset = Dataset(self.records)

    def test_by_qid(self):
        results = self.dataset.by_qid("72")
        self.assertEqual(len(results), 3)

    def test_by_qid_and_group(self):
        results = self.dataset.by_qid_and_group("72", "Total")
        self.assertEqual(len(results), 3)

    def test_underclass_percent(self):
        result = self.dataset.underclass_percent("Total")
        self.assertAlmostEqual(result, 50.0)

    def test_upperclass_percent(self):
        result = self.dataset.upperclass_percent("Total")
        self.assertAlmostEqual(result, 50.0)

    def test_high_risk_percent(self):
        # High risk = Weekly(10) + Daily(5) = 15
        # Total = 10 + 5 + 5 = 20
        # 15 / 20 = 75%
        result = self.dataset.high_risk_percent("22B12", "Total")
        self.assertAlmostEqual(result, 75.0)

    def test_consequence_percent(self):
        records = [
            make_record("22L3", "Never", "Total", 10),
            make_record("22L3", "Once or twice", "Total", 20),
        ]
        ds = Dataset(records)
        result = ds.consequence_percent("22L3", "Total")
        self.assertAlmostEqual(result, (20/30) * 100)

class TestUsageStats(unittest.TestCase):

    def test_average_frequency_score_basic(self):
        records = [
            make_record("22B12", "Weekly", "Total", 10),
            make_record("22B12", "Monthly", "Total", 5),
        ]
        ds = Dataset(records)

        # (3*10 + 2*5) / 15 = 40/15
        result = average_frequency_score(ds, "22B12", "Total")
        self.assertAlmostEqual(result, 40/15)

    def test_average_frequency_score_zero(self):
        ds = Dataset([])
        self.assertEqual(average_frequency_score(ds, "22B12", "Total"), 0.0)

class TestDemographicStats(unittest.TestCase):

    def test_classify_year(self):
        self.assertEqual(classify_year("1st year undergraduate"), "Underclassmen")
        self.assertEqual(classify_year("4th year undergraduate"), "Upperclassmen")
        self.assertEqual(classify_year("Other"), "Other")

class FakeRecord:
    def __init__(self, response, count):
        self.response = response
        self.count = count

class FakeDataset:
    def __init__(self, mapping):
        self.mapping = mapping

    def by_qid_and_group(self, qid, group):
        return self.mapping.get((qid, group), [])


class TestAcademicStats(unittest.TestCase):

    def test_average_gpa_basic(self):
        # A=4.0 (10), B=3.0 (10)
        # avg = (40 + 30)/20 = 3.5
        ds = FakeDataset({
            ("80", "Total"): [
                FakeRecord("A", 10),
                FakeRecord("B", 10),
            ]
        })

        result = average_gpa(ds, "80", "Total")
        self.assertAlmostEqual(result, 3.5)

    def test_average_gpa_zero_when_no_data(self):
        ds = FakeDataset({})
        self.assertEqual(average_gpa(ds, "80", "Total"), 0.0)


if __name__ == "__main__":
    unittest.main()