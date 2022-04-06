# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
# student_heights = [156, 161,  176, 156, 187, 186, 154]

count = 0
total_height = 0

for height in student_heights:
    count += 1
    total_height += height

average_height = round(total_height/count)

print(f"Average height is {average_height}")