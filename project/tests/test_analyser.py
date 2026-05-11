import unittest
from analytics.analyser import TopStudentsAnalyser

class TestAnalyser(unittest.TestCase):
    def setUp(self):
        self.sample = [
            {"student_id": "1", "final_exam_score": "95", "GPA": "3.8"},
            {"student_id": "2", "final_exam_score": "72", "GPA": "2.5"},
            {"student_id": "3", "final_exam_score": "98", "GPA": "3.9"},
            {"student_id": "4", "final_exam_score": "55", "GPA": "1.8"},
            {"student_id": "5", "final_exam_score": "88", "GPA": "3.5"}
        ]

    def test_result_is_not_empty(self):
        a = TopStudentsAnalyser(self.sample)
        a.analyse()
        self.assertNotEqual(a.result, {})

    def test_total_students(self):
        a = TopStudentsAnalyser(self.sample)
        a.analyse()
        self.assertEqual(a.result["total_students"], 5)

    def test_result_has_required_keys(self):
        a = TopStudentsAnalyser(self.sample)
        a.analyse()
        self.assertIn("top_10", a.result) [cite: 102]

    def test_analyse_twice(self):
        a = TopStudentsAnalyser(self.sample)
        a.analyse()
        res1 = a.result.copy()
        a.analyse()
        self.assertEqual(a.result, res1)