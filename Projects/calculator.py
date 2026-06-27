#########   Welcome to my calculator  ########


def sum(a,b):
    return a + b


def subtract(a,b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a,b):
    return a / b


def power(a,b):
    return a ** b


def floor_division(a,b):
    return a // b



def modulo(a,b):
    return a % b



print("Welcome to the calculator!")
print("===============================")

print("1. Sum")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Floor Division")
print("7. Modulo")
print("8. Exit")

while True:
        choice = input("Enter your choice (1-8): ")

        if choice == '8':
            print("the program is Exit")
            break

        elif choice > '8' or choice  < '1':
            print("choice is out of range")
            continue


        if choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))


            if choice == '1':
                result = sum(num1,num2)
                print(f"Result is : {result}")


            elif choice == '2':
                result = subtract(num1,num2)
                print(f"Result is : {result}")


            elif choice == '3':
                result = multiply(num1,num2)
                print(f"Result is : {result}")


            elif choice == '4':
                result= divide(num1,num2)
                print(f"Result is : {result}")


            elif choice == '5':
                result = power(num1,num2)
                print(f"Result is : {result}")

            elif choice == '6':
                result = floor_division(num1,num2)
                print(f"Result is : {result}")


            elif choice == '7':
                result = modulo(num1,num2)
                print(f"Result is : {result}")


print("Have a Good Day")