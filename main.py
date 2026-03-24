from task_manager import add_task, view_tasks,complete_task,delete_task

def main():
    while True:
        print("\n1. Add Task")
        print("2.View All Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Enter task: ")
            add_task(title)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
           task_id = input("Enter task ID to complete: ")
           complete_task(task_id)

        elif choice == "4":
            task_id = input("Enter task ID to delete: ")
            delete_task(task_id)

        elif choice == "5":
               break

if __name__ == "__main__":
    main()
