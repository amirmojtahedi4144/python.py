x = int(input("enter the first number:"))
y = int(input("enter the second number:"))
max = 0
if x >= y:
    max = x
else:
    max = y
z = int(input("enter the third number:"))
if z >= max:
    max = z
m = int(input("please enter the forth number:"))
if m >= max:
    max = m
print(max)