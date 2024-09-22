# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲

import random as r

coin = r.randint(0, 1)
output = ""

if coin == 0:
    output = "Tails"
else:
    output = "Heads"

print(f"It's a {output}")
