import subprocess
import math
subprocess.run("clear")

#Write your code below this line 👇
number_of_cans = 0

def paint_calc(height, width, cover):
    #number of cans = (wall height ✖️ wall width) ÷ coverage per can.
    number_of_cans = math.ceil(height * width / cover)
    print(f"Total amount of cans to use is {number_of_cans}")



#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
