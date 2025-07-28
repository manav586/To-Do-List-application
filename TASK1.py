import json
import os

FILE_NAME = 'tasks.json'

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print("Task added.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "✔️" if task["completed"] else "❌"
        print(f"{idx}. [{status}] {task['description']}")

def delete_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Deleted task: {removed['description']}")
    except IndexError:
        print("Error: Task number does not exist.")

def complete_task(index):
    tasks = load_tasks()
    try:
        tasks[index - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    except IndexError:
        print("Error: Task number does not exist.")

def show_menu():
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            desc = input("Enter task description: ").strip()
            add_task(desc)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            try:
                index = int(input("Enter task number to delete: "))
                delete_task(index)
            except ValueError:
                print("Error: Please enter a valid number.")
        elif choice == '4':
            try:
                index = int(input("Enter task number to mark completed: "))
                complete_task(index)
            except ValueError:
                print("Error: Please enter a valid number.")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

if __name__ == '__main__':
    main()
