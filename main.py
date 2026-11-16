import csv

filePath = "student_test_scores.csv"
students = [

]
try:
    with open(filePath, "r", newline="") as file:
        content = csv.DictReader(file)
        next(content)
        for line in content:
            students.append(line)
except FileNotFoundError:
    print("The CSV list was not found.")
    exit()

print(students)