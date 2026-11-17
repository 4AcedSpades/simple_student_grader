import csv
import numpy

filePath = "student_test_scores.csv"
students = {}
passed = []
failed = []
fieldnames=["Student", "Test Score"]
try:
    with open(filePath, "r", newline="") as file:
        content = csv.DictReader(file)
        for line in content:
            students.update({line["Student"]:line["Test Score"]})
except FileNotFoundError:
    print("The CSV list was not found.")
    exit()

def passing(list):
    for key, val in list.items():
        if int(val) >= 70:
            passed.append({"Student":key,"Test Score":val})
        else:
            failed.append({"Student":key,"Test Score":val})
    return passed, failed

passing(students)

with open("passing_students.csv", "w", newline = "") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(passed)

with open("failed_students.csv", "w", newline = "") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(failed)

def get_results(students):
    mean = 0
    asc = {key: val for key, val in sorted(students.items(), key= lambda item: item[1])}
    print(f"Highest Score: {list(asc.items())[1]}")
    print(f"Lowest Score: {list(asc.items())[0]}")
    for val in asc.values():
        mean += int(val)
    mean = mean/len(asc)
    print(f"The average of all Scores: {mean}")

get_results(students)