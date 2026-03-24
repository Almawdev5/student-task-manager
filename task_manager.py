from storage import load_tasks, save_tasks

def add_task(title):
    tasks = load_tasks()

    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print("✅ Task added successfully!")


def view_tasks():
    tasks = load_tasks()

    if not tasks:
        print("📭 No tasks found.")
        return

    for task in tasks:
        status = "✅" if task["completed"] else "❌"
        print(f'{task["id"]}. {task["title"]} [{status}]')
        
def complete_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == int(task_id):
            task["completed"] = True
            save_tasks(tasks)
            print("✅ Task marked as completed!")
            return

    print("❌ Task not found!")
def delete_task(task_id):
    tasks = load_tasks()

    updated_tasks = [task for task in tasks if task["id"] != int(task_id)]

    if len(tasks) == len(updated_tasks):
        print("❌ Task not found!")
        return

    save_tasks(updated_tasks)
    print("🗑️ Task deleted successfully!")