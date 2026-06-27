#########  Calculation average height of students  #########


student_heights = input("Enter the heights of students separated by spaces: ").split()


for i in range(len(student_heights)):
    student_heights[i] = int(student_heights[i])


total_height = sum(student_heights)


average_height = total_height / len(student_heights)


print(f"The average height of the students is: {average_height}")


print("Have a nice day!")