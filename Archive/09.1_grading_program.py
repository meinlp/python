import subprocess
subprocess.run("clear")

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

student_grades = {}
for student in student_scores:
    if 90 < student_scores[student] <= 100:
        student_grades[student] = "Outstanding"
    elif 80 < student_scores[student] <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif 70 < student_scores[student] <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


# 🚨 Don't change the code below 👇
print(student_grades)
