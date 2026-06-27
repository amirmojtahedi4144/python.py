word = input("enter the word:")
x = ""
y = "aeiouAEIOU"
for i in word:
    if i not in y:
        x += i
print(x)