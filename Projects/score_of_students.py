########### Welcome to the student grade management system ###########
import csv

def add_student():
    with open("final_grades.csv", "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        writer.writerow([name, grade])
        print(f"Student {name} with grade {grade} added successfully.")
        
def show_all():
    with open("final_grades.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        print("List of all students and their grades:")
        for row in reader:
            print(f"Student {row[0]} has a grade of {row[1]}")
            
def show_average():
    with open("final_grades.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        grades = [int(row[1]) for row in reader]
        average = sum(grades) / len(grades)
        print(f"The average grade is {average}")
        
while True:
    print("1. Add student")
    print("2. Show all students")
    print("3. Show average grade")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        show_all()
    elif choice == "3":
        show_average()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
        
print("Thank you for using the student grade management system!")