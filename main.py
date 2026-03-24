from task_manager import add_task

def main():
    while True:
        print("\n1. Add Task")
        print("2. Exit")

        choice = input("Choose: ")

        if choice == "1":
            title = input("Enter task: ")
            add_task(title)

        elif choice == "2":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()