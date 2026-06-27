x = []
print("Enter numbers one by one (enter END to finish):")
while True:
    number = input()
    if number == "END":
        break
    x.append(number)
for i in x[::-1]:
    print(i[::-1])