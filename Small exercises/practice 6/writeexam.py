import os
def soalsaz(exam_name,name_professor,subject,date):
    if os.path.exists(f"D:/class python/practice 6/exams/{exam_name}.txt"):
        return "this exam already exists"
    else:
        x = open(f"D:/class python/practice 6/exams/{exam_name}.txt" , "w")
        x.write(f"name professor = {name_professor} , subject = {subject} , date = {date} , name student = \n")
        counter = 1
        while True:
            soal=input("enter the soal: ")
            if soal == "END":
                print("tamam")
                break
            javab = input("enter the answers with comma: ").split(",")
            score = input("enter the score: ")
            questions = (f"{counter}.{soal}({score} score)\n"
                         f"1){javab[0]} 2){javab[1]} 3){javab[2]} 4){javab[3]}\n")
            x.write(f"{questions}")
        counter += 1
        print(f"you wrote {counter -1} questions")
        answers = input("enter the answers with a comma between")
        x.write(f"{answers}")
        x.close()
        return "exam has been made"
if __name__ == "__main__":
    soalsaz("exam","name","1404","12")