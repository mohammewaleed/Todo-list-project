import sys
add_task =[]
commands = ["remove", "add", "view", "exit"]
while True:
    user_command = input(f"Enter a command from {commands}: ").lower()

    if user_command == "add":
        task =input("Enter your task with  ")
        add_task.append(task)
        print("task is added")

    elif user_command == "view":
      if not add_task :
        print("there are not tasks")
      else:
        for task in add_task :
          print(task)

    elif user_command == "remove":
      if not add_task :
        print("there are no tasks")
      else:
        task = input("Enter your task that you want remove: ")
        if task in add_task:
          add_task.remove(task)
          print("it removed")
        else:
          print("your task not founded")
    elif user_command == "exit":
      break
    else:
      print("Invalid command. Please enter again.")
