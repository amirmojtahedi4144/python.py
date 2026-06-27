total = 0
print("Enter numbers one by one (enter 0 to finish):")
while True:
    number = int(input(""))
    if number == 0:
        break
    total += number
print("Sum of all numbers:", total)