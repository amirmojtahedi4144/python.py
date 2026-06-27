import os
def ezafekardanbesoal(esm_soal:str):
    if not os.path.exists("List_soalat.txt"):
        with open("List_soalat.txt", "w") as f:
            f.write(esm_soal)
    else:
        with open("List_soalat.txt", "r") as f:
            x = f.read().split("\n")
            if esm_soal in x:
                return f"barge emtehani {esm_soal} vogood darad,ye soal dige bezan ya soal ro hazf kon\n"
            else:
                x.append(esm_soal)
        with open("List_soalat.txt", "w") as f:
            for i in range(len(x)):
                f.write(x[i])
                if i < len(x)-1:
                    f.write("\n")
if __name__ == "__main__":
    ezafekardanbesoal("math4")