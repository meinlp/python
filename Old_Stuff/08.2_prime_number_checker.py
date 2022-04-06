
#Write your code below this line 👇
import subprocess
subprocess.run("clear")

def prime_checker(number):
    flag = 0
    for i in range(number):
        if number % (i + 1) == 0:
            flag += 1
    if flag <= 2:
        print("It's a prime number!")
    else:
        print("It is not a prime number")


#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
