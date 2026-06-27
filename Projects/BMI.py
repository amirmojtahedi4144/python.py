##########   Welcome To My BMI  ##########


height = float(input("Enter your height in meters : "))


weight = int(input("Enter your weight in kg : "))


bmi = weight / height ** 2


bmi_as_int = int(bmi)


print(f"Your BMI is : {bmi}")


print(bmi_as_int)


if bmi < 18.5:
    print("You are underweight.")
    
    
    
elif bmi < 25:
    print("You are normal weight.")
    
    
    
elif bmi < 30:
    print("You are overweight.")
    
    
    
    
elif bmi < 35:
    print("You are obese.")
    
        
else:
    print("You are clinically obese.")
    


print("Thank you for using the BMI calculator!")