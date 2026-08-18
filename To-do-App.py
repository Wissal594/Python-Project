print("===== TO-DO APP =====\n \n1. Add task\n2. Show tasks\n3. Complete task\n4. Delete task\n5. Exit")
tasks=[]
def delete_tasks(b):
    del tasks[b-1]
    print( f"Task deleted successfully")

while True:
    n = int(input("Enter your choice: "))

    if n==1:
        task=input("Enter a task: ")
        tasks.append(task)
        print("Task added")
    elif n==2:
        if not tasks:
            print("No tasks added")
        else:
            print("=== Your Tasks ===")
            for i ,ta in enumerate(tasks,1):
                print(f"Task {i} is {ta}")
    elif n==3:
        a=int(input("enter the number of the  task you completed"))
        if a>len(tasks):
           print("no task is added under this number")
        else :
           print(f"task completed✅:{tasks[a-1]}")
           delete_tasks(a)
    elif n==4:
        b=int(input("enter the number of the  task you want to delete"))
        delete_tasks(b)
    elif n==5:
        response=input("Are you sure you want to exit the program? (y/n)")
        if response.upper()=="Y":
            print("You have exited the program")
            print("Thank you for using this program")
            break
        else:
            continue
    else :
        print("Invalid input")
        continue








