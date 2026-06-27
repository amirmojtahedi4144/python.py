#########   Welcome  ########




task_list = []


def add_list():
    task = input("Enter your Task: ")
    task_list.append(task)
    print("Add Task")    
    
    
    
    
def delete_list():
    view_list()
    num_task = int(input("Enter the task number: "))
    removed_list = task_list.pop()
    print(f"You have removed {removed_list}")
    
    
    
def view_list():
    if len(task_list) == 0:
        print("No tasks avlaible")
    else:
        print("----Your ToDo List----")
        for i in range(len(task_list)):
            print(str(i+1)+ "." + task_list[i])
            print()    
    
        
    
    
    
while True:
    print("1. Add to list")
    print("2. View list")
    print("3. Delete from list")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '4':
        print("Exiting the program.")
        break

    elif choice > '4' or choice < '1':
        print("Choice is out of range.")
        continue

    if choice == '1':
        add_list()
    elif choice == '2':
        view_list()
    elif choice == '3':
        delete_list()
        
        
print("Have a Good Day")