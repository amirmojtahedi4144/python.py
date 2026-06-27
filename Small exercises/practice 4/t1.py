x = input("enter the name:")
temp = ""
for i in x:
    if i in temp:
        continue
    else:
        temp = temp + i
print(temp)
print(len(temp))