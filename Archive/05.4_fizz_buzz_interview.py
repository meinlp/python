output = ''
for number in range(1, 101):
    if number % 3 == 0:
        output = "Fizz"
        if number % 5 ==0:
            output += "Buzz"
    elif number % 5 == 0:
        output = "Buzz"
    else:
        output = number
    print(output)
    output = ''
