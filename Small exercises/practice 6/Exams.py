import os
if not os.path.exists("List_soalat.txt"):
    with open("List_soalat.txt","w")as f:
        f.write("")
else:
    with open("List_soalat.txt","r")as f:
        x = f.read().split("\n")
        x.append("")
    with open("List_soalat.txt","w")as f:
        for i in x:
            f.write(i)