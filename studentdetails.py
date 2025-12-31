# studentdetails.py
import sys

def main():
    # Check for correct number of arguments
    if len(sys.argv) != 7:
        print("Usage: python studentdetails.py <name> <department> <semester> <marks1> <marks2> <marks3>")
        sys.exit(1)

    name = sys.argv[1]
    department = sys.argv[2]
    semester = sys.argv[3]
    marks1 = int(sys.argv[4])
    marks2 = int(sys.argv[5])
    marks3 = int(sys.argv[6])

    average = (marks1 + marks2 + marks3) / 3

    if average >= 90 and average <= 100:
        grade = "S"
    elif average >= 80:
        grade = "A"
    elif average >= 65:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    print("***** STUDENT DETAILS *****")
    print("Name       :", name)
    print("Department :", department)
    print("Semester   :", semester)
    print("Average    :", round(average, 2))
    print("Grade      :", grade)

if __name__ == "__main__":
    main()
