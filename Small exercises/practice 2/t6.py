temprature = int(input("enter the temprature:"))
if temprature > 100:
    print("steam")
elif temprature < 0:
    print("ice")
else:
    print("water")