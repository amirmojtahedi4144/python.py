def calc(number1:int,number2:int)->int:
    op = input("enter the op:")
    if op == "+":
        number1 = number1 + number2
    elif op == "-":
        number1 = number1 - number2
    elif op == "*":
        number1 = number1 * number2
    elif op == "/":
        number1 = number1 / number2
    elif op == "//":
        number1 = number1 // number2
    elif op == "%":
        number1 = number1 % number2
    elif op == "**":
        number1 = number1 ** number2
    print(number1)
number1 = int(input())
number2 = int(input())
while True:
    calc(number1,number2)