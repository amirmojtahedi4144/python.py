x = input("enter the code:")
lower_x = x.lower()
if lower_x.endswith("-tmp"):
    x = x[:-4]
    print(x)
    number_part = x[3:]
    if len(number_part) == 6 and number_part.isdigit():
        print("کد معتبر:", "ID-" + number_part)
    else:
        print("کد نامعتبر است")
print(x)
print(len(x))