
import sys
import pytest
from  studentdetails import calculate_grade, main


# 🔹 Grade S (90–100)
@pytest.mark.parametrize("marks", [90, 95, 100])
def test_grade_S(marks):
    assert calculate_grade(marks) == "S"


# 🔹 Grade A (80–89)
@pytest.mark.parametrize("marks", [80, 85, 89])
def test_grade_A(marks):
    assert calculate_grade(marks) == "A"


# 🔹 Grade B (65–79)
@pytest.mark.parametrize("marks", [65, 72, 79])
def test_grade_B(marks):
    assert calculate_grade(marks) == "B"


# 🔹 Grade C (50–64)
@pytest.mark.parametrize("marks", [50, 57, 64])
def test_grade_C(marks):
    assert calculate_grade(marks) == "C"


# 🔹 Grade D (40–49)
@pytest.mark.parametrize("marks", [40, 45, 49])
def test_grade_D(marks):
    assert calculate_grade(marks) == "D"


# 🔹 Grade F (Below 40)
@pytest.mark.parametrize("marks", [0, 25, 39])
def test_grade_F(marks):
    assert calculate_grade(marks) == "F"


# 🔹 Test main() using sys.argv (same as your first code)
def test_main_output(monkeypatch, capsys):
    test_args = [
        "Studentdetails.py",
        "mahek",
        "Integrated MCA",
        "3",
        "85",
        "78",
        "90"
    ]

    # Mock command-line arguments
    monkeypatch.setattr(sys, "argv", test_args)

    # Run main
    main()

    # Capture output
    output = capsys.readouterr().out

    assert "GRADING CRITERIA" in output
    assert "STUDENT DETAILS" in output
    assert "Name       : mahek" in output
    assert "Department : Integrated MCA" in output
    assert "Semester   : 3" in output
    assert "Average    : 84.33" in output
    assert "Grade      : A" in output