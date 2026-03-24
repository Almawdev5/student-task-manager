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