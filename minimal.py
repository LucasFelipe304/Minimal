from datetime import date, datetime
import os

def get_username():
    return os.getlogin()

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
index_day()

