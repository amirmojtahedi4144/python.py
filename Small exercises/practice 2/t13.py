zel1 , zel2 , zel3 = map(int,input().split())
if (zel1 + zel2) > zel3 and (zel1 + zel3) > zel2 and (zel2 + zel3) > zel1:
    print("bale")
else:
    print("na")