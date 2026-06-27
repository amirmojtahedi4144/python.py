x = int(input("enter the first number:"))
y = int(input("enter the second number:"))
min = 0
if x <= y:
    min = x
else:
    min = y
z = int(input("enter the third number:"))
if z <= min:
    min = z
m = int(input("enter the forth number:"))
if m <= min:
    min = m
print(min)