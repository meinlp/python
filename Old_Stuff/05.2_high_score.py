# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
# student_scores = "78 65 89 86 55 91 64 89".split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score = 0

for current_score in student_scores:
    if current_score > highest_score:
        highest_score = current_score
print(f"The highest score in the class is {highest_score}")



