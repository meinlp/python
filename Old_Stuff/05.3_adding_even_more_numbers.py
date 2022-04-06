total = 0

# for i in range(2, 101, 2):
#     total += i

for number in range(1, 101):
    if number % 2 == 0:
        total+= number
print(total)