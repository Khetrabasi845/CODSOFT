to_do_list_app = {}
def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Update a Task")
    print("4. Delete a Task")
    print("5. Exit")

def add_task():
    task_id = len(to_do_list_app) + 1
    task_name = input("Enter the task name: ")
    to_do_list_app[task_id] = task_name
    print(f"Task '{task_name}' added successfully.")

def view_tasks():
    if not to_do_list_app:
        print("No tasks available.")
    else:
        print("\n--- To-Do List ---")
        for task_id, task_name in to_do_list_app.items():
            print(f"{task_id}. {task_name}")

def update_task():
    view_tasks()
    try:
        task_id = int(input("\nEnter the task ID to update: "))
        if task_id in to_do_list_app:
            new_task_name = input("Enter the new task name: ")
            to_do_list_app[task_id] = new_task_name
            print(f"Task {task_id} updated successfully.")
        else:
            print("Invalid Task ID.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_id = int(input("\nEnter the task ID to delete: "))
        if task_id in to_do_list_app:
            deleted_task = to_do_list_app.pop(task_id)
            print(f"Task '{deleted_task}' deleted successfully.")
        else:
            print("Invalid Task ID.")
    except ValueError:
        print("Please enter a valid number.")

# Main Program Loop
while True:
    show_menu()
    choice = input("\nEnter your choice (1-5): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting the To-Do List application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")