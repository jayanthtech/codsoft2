class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed successfully.")
        else:
            print("Task not found.")

    def show_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks in the list.")

    def update_task(self, index, updated_task):
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1] = updated_task
            print("Task updated successfully.")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Update Task")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == 2:
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == 3:
            todo_list.show_tasks()
        elif choice == 4:
            index = int(input("Enter the task index to update: "))
            updated_task = input("Enter the updated task: ")
            todo_list.update_task(index, updated_task)
        elif choice == 5:
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
