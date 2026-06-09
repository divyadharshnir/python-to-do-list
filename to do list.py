# TO-DO LIST PROJECT

my_tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter the task: ")
        my_tasks.append(task)
        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(my_tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(my_tasks, start=1):
                print(f"{i}. {task}")

    # Remove Task
    elif choice == "3":
        if len(my_tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i, my_task in enumerate(my_tasks, start=1):
                print(f"{i}. {my_task}")

            remove_task = int(input("Enter task number to remove: "))

            if 1 <= remove_task <= len(my_tasks):
                removed = my_tasks.pop(remove_task - 1)
                print(f"'{removed}' removed successfully!")
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "4":
        print("Exiting To-Do List...")
        break

    else:
        print("Invalid choice. Please try again.")
