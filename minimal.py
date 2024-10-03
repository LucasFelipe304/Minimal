from datetime import datetime, date
import os

def get_username():
    return os.getlogin()
def line():
    print('-' * 25)
def current_time():
    return datetime.now()
def saudation():
    current_time = datetime.now()
    hour = current_time.hour

    if 5 <= hour < 12:
        print (f"Good Morning, {os.getlogin()}!")
    elif 12 <= hour < 18:
        print (f"Good afternoon, {os.getlogin()}!")
    else:
        print (f"Good night, {os.getlogin()}!")

def index_day():
    current_day = date.today().weekday()
    if current_day == 0:
        return('Monday')
    elif current_day == 1:
        return('Tuesday')
    elif current_day == 2:
        return('Wednesday')
    elif current_day == 3:
        return('Thursday')
    elif current_day == 4:
        return('Friday')
    elif current_day == 5:
        return('Saturday')
    else:
        return('Sunday')
def daily_info():
    day_informations = current_time()
    print('Day informations -> ', index_day(), day_informations)

def menu():
    menu = (
        "1 - Add Task\n"
        "2 - Delete Task\n"
        "3 - Change Task\n"
        "4 - View List" 
        "5 - Exit"
    )
    print(menu)

saudation()
daily_info()
line()
menu()

def type_choice():
    type_user = str(input("~~~> ")).strip()
    return type_user

task_list = []

while True:
    type_user = type_choice()
    def handle_choice(type_user):

        if type_user == '1':
            print('||| Add Task')
            type_addtask = str(input("Type: ")).strip().lower()
            task_list.append(type_addtask)
            print('-' * 4, 'Task Added.')
            
        elif type_user == '2':
            if len (task_list) > 0:
                print('||| Delete Task')
                for index, task in enumerate(task_list):
                    print(f"{index}:, {task}")

                try:
                    type_deletetask = int(input('Type the index of the item you want to delete: '))
                    if 0 <= type_deletetask < len(task_list):
                        task_list.pop(type_deletetask)
                        print('-' * 4, 'Task Deleted.')
                    else:
                        print("Invalid index.")
                except ValueError:
                    print("Please enter a valid number.")

            else:
                print("No tasks to delete.")

        elif type_user == '3':
            if len(task_list) > 0:
                print("||| Change Task")
                for index, task in enumerate(task_list):
                    print(f"{index}: {task}")
                try:
                    type_changetask = int(input('Type the index of the item you want to change: '))
                    if 0 <= type_changetask < len(task_list):
                        new_task = input('Enter new task: ').strip().lower()
                        task_list[type_changetask] = new_task
                        print('-' * 4, 'Task Updated.')
                    else:
                        print("Invalid index.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No tasks to change.")
        
        elif type_user == '5':
            print("Exiting...")
            return False
        
        elif type_user == "4":
            if len(task_list) > 0:
                print("||| View List")
                for index, item in enumerate(task_list):
                    print(f"{index}: {item}")
            else:
                print("The list is empty.")
        else:
            print("Invalid choice!")
        return True
    
    
    if not handle_choice(type_user):
        break