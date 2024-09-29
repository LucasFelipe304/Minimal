from datetime import datetime, date
import os

def get_username():
    return os.getlogin()
def line():
    print('-' * 25)
def constant_days(): 
    DAYS = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
]
    return DAYS
def current_time():
    return datetime.now()
def saudation():
    current_time = datetime.now()
    hour = current_time.hour

    if 5 <= hour < 12:
        print (f"Good Morning, {os.getlogin()}!")
    if 12 <= hour < 18:
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
        "4 - Exit"
    )
    print(menu)

saudation()
daily_info()
line()
menu()

def type_choice():
    type_user = str(input("~~~> ")).strip()
    return type_user

type_user = type_choice()

def handle_choice(type_user):
    if type_user == '1':
        print('|| Add Task')
        type_addtask = str(input("Type: ")).strip().lower()
    else:
        print("Invalid choice!")

handle_choice(type_user)