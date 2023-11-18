import sys

tasks = []

def add_task():
    task = input("Enter your task: ")
    tasks.append(task)
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("There are no tasks.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def remove_task():
    if not tasks:
        print("There are no tasks to remove.")
    else:
        view_tasks()
        try:
            task_index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                print(f"Task '{removed_task}' removed successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    commands = ["add", "view", "remove", "exit"]

    while True:
        user_command = input(f"Enter a command from {commands}: ").lower()

        if user_command == "add":
            add_task()
        elif user_command == "view":
            view_tasks()
        elif user_command == "remove":
            remove_task()
        elif user_command == "exit":
            sys.exit(0)
        else:
            print("Invalid command. Please enter again.")

if __name__ == "__main__":
    main()
