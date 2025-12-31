import unittest
import subprocess
import sys

class TestStudentGrade(unittest.TestCase):

    def run_program(self, args):
        result = subprocess.run(
            [sys.executable, "studentdetails.py"] + args,
            capture_output=True,
            text=True
        )
        return result.stdout

    def test_grade_S(self):
        output = self.run_program(["Mahek", "BCA", "3", "95", "92", "90"])
        self.assertIn("Grade", output)
        self.assertIn("S", output)

    def test_grade_A(self):
        output = self.run_program(["Mahek", "BCA", "3", "85", "82", "80"])
        self.assertIn("A", output)

    def test_grade_B(self):
        output = self.run_program(["Mahek", "BCA", "3", "70", "68", "66"])
        self.assertIn("B", output)

    def test_grade_C(self):
        output = self.run_program(["Mahek", "BCA", "3", "55", "52", "50"])
        self.assertIn("C", output)

    def test_grade_D(self):
        output = self.run_program(["Mahek", "BCA", "3", "42", "40", "41"])
        self.assertIn("D", output)

    def test_grade_F(self):
        output = self.run_program(["Mahek", "BCA", "3", "30", "35", "38"])
        self.assertIn("F", output)

if __name__ == "__main__":
    unittest.main()