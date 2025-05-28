from typing import List

def add_task(tasks: List[str]) -> None:
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added.")
    else:
        print("Empty task not added.")

def list_tasks(tasks: List[str]) -> None:
    if not tasks:
        print("No tasks available.")
        return
    print("\nTo-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def show_menu() -> None:
    print("\nOptions: add | list | quit")

def todo_app():
    tasks: List[str] = []
    while True:
        show_menu()
        command = input("Command: ").strip().lower()
        if command == "add":
            add_task(tasks)
        elif command == "list":
            list_tasks(tasks)
        elif command == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    todo_app()
