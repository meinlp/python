import random as r

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
# names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


victim_index = r.randint(0, len(names) - 1)
victim = names[victim_index]
print(f"{victim} is going to pay today!")