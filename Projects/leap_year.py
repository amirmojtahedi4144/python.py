##########   Welcome To The Leap Year Calculator   ##########


year = int(input("Enter a year : "))


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    
    
    
    
print("Thank you for using the Leap Year Calculator!")    