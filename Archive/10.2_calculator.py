from extras.calculator_logo import logo
import subprocess

subprocess.run("clear")
print(logo)

# Add
def add(n1, n2):
    return n1 + n2
# Subtract
def subtract(n1, n2):
    return n1 - n2
# Multiply
def multiply(n1, n2):
    return n1 * n2
# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
    ## th1is is for the test purpose ##
    # print(num1, symbol, num2, " is equal to ", (operations[symbol](num1, num2)))
operation_symbol = input("Pick an operator from the list above: ")
num2 = int(input("What's the second number?: "))
result = operations[operation_symbol](num1, num2)

print(f"{num1} {operation_symbol} {num2} = {result}")
we_are_not_end = True

while we_are_not_end:

    ask_for_ending = input(f"Do you want to continue with {result} or end this bullshit? Y/N: ")
    if ask_for_ending.lower() == "n":
        we_are_not_end = False
        print("See ya!")
    elif ask_for_ending.lower() == "y":
        operation_symbol = input("Pick an operator: ")
        num3 = int(input("What's the number?: "))
        num4 = result
        result = operations[operation_symbol](num3, num4)
        subprocess.run("clear")
        print(f"{num3} {operation_symbol} {num4} = {result}")
    else:
        print("R U mad, bro?")