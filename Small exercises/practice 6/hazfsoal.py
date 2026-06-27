import os
def hazfsoal(address:str):
    with open("List_soalat.txt","r")as f:
        z = f.read().split("\n")
    z.remove(address)
    with open("List_soalat.txt", "w") as f:
        for i in z:
            f.write(i)
    os.remove(f"exams/{address}")
if __name__ == "__main__":
    hazfsoal("math4.txt")