score = float(input("enter the score:"))
if 0 <= score <=20:
    if score >= 10:
        print("pass")
    else:
        print("fail")
else:
    print("invalid input")