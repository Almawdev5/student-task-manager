from task_manager import add_task, view_tasks

def main():
    while True:
        print("\n1. Add Task")
        print("2.Show Tasks")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            title = input("Enter task: ")
            add_task(title)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()