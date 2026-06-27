x1 , x2 , x3 = map(int,input().split())
if (x1 + x2 + x3) == 180 and x1 > 0 and x2 > 0 and x3 > 0:
    print("triangle can be drawn")
if x1 == x2 == x3 == 60:
    print("متساوی الاضلاع")
elif x1 == 90 or x2 == 90 or x1 == 90:
    print("قایم الزاویه")
elif x1 == x2 or x2 == x3 or x1 == x3:
    print("متساوی الساقین")
else:
    print("can't make a triangle")