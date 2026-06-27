##########    Welcome To The Age Calculator1    ##########

current_year = int(input("Enter the current year : "))
birth_year = int(input("Enter your birth year : "))
age = current_year - birth_year
print(f"Your age is : {age}")

if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")



print("Thank you for using the Age Calculator!")
#################################################################


##########   Welcome To The Age Calculator2    ##########

age = int(input("Enter your current age : "))


years_reamaining = 90 - age

days_remaining = years_reamaining * 365

weeks_remaining = years_reamaining * 52

months_remaining = years_reamaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left until you turn 90 years old.")


print("Thank you for using the Age Calculator!")