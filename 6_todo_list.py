filename = "tasks.txt"


def load_tasks():
    tasks = []

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if line.startswith("[x] "):
                    tasks.append({"task": line[4:], "complete": True})
                elif line.startswith("[ ] "):
                    tasks.append({"task": line[4:], "complete": False})
                elif line != "":
                    tasks.append({"task": line, "complete": False})
    except FileNotFoundError:
        pass

    return tasks


def save_tasks(tasks):
    with open(filename, "w") as file:
        for task in tasks:
            if task["complete"]:
                file.write("[x] " + task["task"] + "\n")
            else:
                file.write("[ ] " + task["task"] + "\n")


def show_tasks(tasks):
    print("Your Tasks:")
    print("------------------------------------------")

    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        for i in range(len(tasks)):
            if tasks[i]["complete"]:
                status = "Done"
            else:
                status = "Todo"

            print(str(i + 1) + ".", "[" + status + "]", tasks[i]["task"])

    print("------------------------------------------")


tasks = load_tasks()

while True:
    print("===TODO LIST===")
    print("------------------------------------------")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task complete")
    print("4. Edit task")
    print("5. Save tasks")
    print("6. Quit")
    print("------------------------------------------")

    choice = input("Choose: ")
    print("------------------------------------------")

    if choice == "1":
        task = input("Task: ").strip()

        if task == "":
            print("Task cannot be empty.")
        else:
            tasks.append({"task": task, "complete": False})
            save_tasks(tasks)
            print("Task added and saved.")

    elif choice == "2":
        show_tasks(tasks)

    elif choice == "3":
        show_tasks(tasks)

        if len(tasks) > 0:
            try:
                task_number = int(input("Task number to complete: "))

                if task_number < 1 or task_number > len(tasks):
                    print("Invalid task number.")
                else:
                    tasks[task_number - 1]["complete"] = True
                    save_tasks(tasks)
                    print("Task marked complete and saved.")
            except ValueError:
                print("Please enter a valid task number.")

    elif choice == "4":
        show_tasks(tasks)

        if len(tasks) > 0:
            try:
                task_number = int(input("Task number to edit: "))

                if task_number < 1 or task_number > len(tasks):
                    print("Invalid task number.")
                else:
                    new_task = input("New task: ").strip()

                    if new_task == "":
                        print("Task cannot be empty.")
                    else:
                        tasks[task_number - 1]["task"] = new_task
                        save_tasks(tasks)
                        print("Task edited and saved.")
            except ValueError:
                print("Please enter a valid task number.")

    elif choice == "5":
        save_tasks(tasks)
        print("Tasks saved to", filename)

    elif choice == "6":
        save_tasks(tasks)
        print("Tasks saved. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

    print("------------------------------------------")
