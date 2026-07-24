############  WELCOME TO THE FOR LOOP PROJECT ############
name = input("Enter your name: ")

name = name.lower()

name = name.replace(" ", "")

b = []
for i in name:
    if i not in b:
        print(f"your name has {name.count(i)} {i}")
        b.append(i)
        
print("====================================")
print("Thank you for using the for loop project!")
print("Have a great day!")