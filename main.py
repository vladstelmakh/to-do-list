from todo_list import Task, TodoList

def main():
    todo_list = TodoList()  # Створення об'єкта списку завдань

    while True:
        print("\n1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Show Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task = Task(title, description)
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == "3":
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.mark_task_completed(index)
        elif choice == "4":
            for i, task in enumerate(todo_list.tasks, 1):
                print(f"{i}. {task}")
        elif choice == "5":
            break
        else:
            print("Invalid option.")
if __name__ == "__main__":
    main()

