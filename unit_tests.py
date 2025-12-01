import unittest
from classes import Student, Community
from data_reader import read_student_line

class TestStudent(unittest.TestCase):
    def test_wellness_score(self):
        s = Student("Alice F", 7, 4, 3)
        score, label = s.wellness_score()
        self.assertEqual(label, "Moderate")
        self.assertIsInstance(score, float)

class TestCommunity(unittest.TestCase):
    def test_compute_averages(self):
        students = [
            Student("Alice F", 7, 4, 3),
            Student("Kara U", 6, 5, 8)
        ]
        c = Community(students)
        c.compute_averages()
        self.assertAlmostEqual(c.summary["avg_sleep"], 6.5)
        self.assertAlmostEqual(c.summary["avg_study"], 4.5)
        self.assertAlmostEqual(c.summary["avg_stress"], 5.5)

class TestDataReader(unittest.TestCase):
    def test_read_student_line(self):
        s = read_student_line("Alice F, 7, 4, 3", 1)
        self.assertEqual(s.name, "Alice F")
        self.assertEqual(s.sleep_hours, 7)

if __name__ == '__main__':
    unittest.main()