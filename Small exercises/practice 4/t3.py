databank = []
while True:
    x = input()
    if x.lower() == "end":
        break
    databank.append(int(x))
databank.reverse()
print(databank)