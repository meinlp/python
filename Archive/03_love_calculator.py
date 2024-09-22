# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# name1 = "azazaerwer"
# name2 = "adfadsfadf"

name1_lower = name1.lower()
name2_lower = name2.lower()

first_digit = 0
second_digit = 0

for letter in "true":
    first_digit += name1_lower.count(letter) + name2_lower.count(letter)
for letter in "love":
    second_digit += name1_lower.count(letter) + name2_lower.count(letter)

result = str(first_digit) + str(second_digit)

# interpretate result:
result = int(result)
if (result > 90) or (result < 10):
    print(f"Your score is {result}, you go together like ur mom.")
elif (result > 40) and (result < 50):
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")