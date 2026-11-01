def show_menu():
    print("\n== TO-DO LIST ==")
    print("1. Add Task ")
    print("2. view Task")
    print("3. update Task")
    print("4. Remove Task")
    print("5. Exit")
    print()

todo_list = []

def Add_task():
    Task = input("Enter your task: ").strip()

    if Task:
        if Task not in todo_list:
            todo_list.append(Task)
            print(f"task Added: {Task}")
        else:
            print("task already exists in list.")
    else:
        print("task canot be empty.")

def view_task():

    if todo_list:
        print("\nYour To-DO List: ")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")
    else:
        print("task is empty")

def update_task():
    if todo_list:
        view_task()
        task_No = input("\n Enter your num to update: ").strip()
        if task_No.isdigit():
            task_No = int(task_No)

            if 1 <= task_No <= len(todo_list):
                new_task = input("\nEnter New Task: ").strip()

                if new_task:
                    old_task = todo_list[task_No -1]
                    todo_list[task_No -1] = new_task
                    print(f"Task updated: {old_task} -> {new_task}")
                else:
                    print("Task cannot be empty")
            else:
                print("Invalid task number")
        else:
            print("plz enter a valid num.")
    else:
        print("No task to update")

def  Remove_task():
    if todo_list:
        view_task()
        task_No = input("\n Enter task number to removed: ").strip()

        if task_No.isdigit():
            task_No = int(task_No)
            
            if 1 <= task_No <= len(todo_list):
                Remove_task = todo_list.pop(task_No -1)
                print(f"removed: {Remove_task}")
            else:
                print("invalid task number")
        else:
            print("plz Enter the valid num.")        
    else:
        print("NO taks to remove")             

while True:
    show_menu()
    choice = input("Enter your choice: ").strip()
    
    match choice:
        case "1":
            Add_task()
        case "2":
            view_task()
        case "3":
            update_task()
        case "4":
            Remove_task()
        case "5":
            print("Exit TO DO List")
            break
        case _:
            print("Invalid choice. pls select from menu.")