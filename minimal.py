from datetime import datetime, date
import os

# Global constants
DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def get_username():
    """Returns the system's username."""
    return os.getlogin()

def space():
    """Prints a space to separete lines."""
    print() 

def current_time():
    """Returns the current date and time."""
    return datetime.now()

def greeting():
    """Displays a greeting based on the current time of day."""
    hour = current_time().hour

    if 5 <= hour < 12:
        print(f"Good Morning, {get_username()}!")
    elif 12 <= hour < 18:
        print(f"Good Afternoon, {get_username()}!")
    else:
        print(f"Good Night, {get_username()}!")

def current_day():
    """Returns the current day of the week as a string."""
    today_index = date.today().weekday()
    return DAYS_OF_WEEK[today_index]

def daily_info():
    """Displays today's date and current time information."""
    print("Day information ->", current_day(), current_time())
    space()
def display_menu():
    """Displays the option menu."""
    menu = (
        "1 - Add Task\n"
        "2 - Delete Task\n"
        "3 - Change Task\n"
        "4 - View List\n"
        "5 - Exit\n"
    )
    print(menu)
    space()

def get_user_choice():
    """Captures and returns the user's choice."""
    return input("~~~> ").strip()

def display_tasks(task_list):
    """Displays the list of tasks."""
    if not task_list:
        print("No tasks available.")
    else:
        for index, task in enumerate(task_list):
            print(f"{index}: {task}")
    space()


def add_task(task_list):
    """Adds a new task to the task list."""
    new_task = str(input("Type the new task: ").strip().lower())
    if new_task.isalpha():
        task_list.append(new_task)
        print("---- Task Added.")
        space()
    else:
        print("Type only caracteres.")

def delete_task(task_list):
    """Removes a task from the task list by index."""
    if task_list:
        display_tasks(task_list)
        try:
            task_index = str(input("Type the index of the task to delete: "))
            if task_index.isnumeric():
                task_index = int(task_index)
                if 0 <= task_index < len(task_list):
                    task_list.pop(task_index)
                    print("---- Task Deleted.")
                    space()
                else:
                    print("Invalid index.")
                    space()
            else:
                print("Invalid index.")
                space()
                
        except ValueError:
            print("Please enter a valid number.")
            space()

    else:
        print("No tasks to delete.")
        space()

def change_task(task_list):
    """Updates an existing task by index."""
    if task_list:
        display_tasks(task_list)
        try:
            task_index = int(input("Type the index of the task to change: "))
            if 0 <= task_index < len(task_list):
                new_task = input("Enter the new task: ").strip().lower()
                task_list[task_index] = new_task  # Corrected this line
                print("---- Task Updated.")
                space()
            else:
                print("Invalid index.")
                space()
        except ValueError:
            print("Please enter a valid number.")
            space()
    else:
        print("No tasks to change.")
        space()

def view_list(task_list):
    """Displays the task list."""
    display_tasks(task_list)  # Updated to use display_tasks
    space()

def handle_choice(choice, task_list):
    """Handles the user's choice and calls the corresponding function."""
    if choice == "1":
        add_task(task_list)
    elif choice == "2":
        delete_task(task_list)
    elif choice == "3":
        change_task(task_list)
    elif choice == "4":
        view_list(task_list)
    elif choice == "5":
        return False
    else:
        print("Invalid choice!")
    return True

def main():
    """Main function to run the program."""
    task_list = []

    # Display greeting and daily information
    greeting()
    daily_info()

    while True:
        display_menu()
        choice = get_user_choice()
        if not handle_choice(choice, task_list):
            print("Exiting...")
            break

# Runs the program.
if __name__ == "__main__":
    main()
