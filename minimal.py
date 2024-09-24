from datetime import date

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

def IndexDay():
    current_day = date.today().weekday()
    if current_day == 0:
        print('Monday')
    elif current_day == 1:
        print('Tuesday')
    elif current_day == 2:
        print('Wednesday')
    elif current_day == 3:
        print('Thursday')
    elif current_day == 4:
        print('Friday')
    elif current_day == 5:
        print('Saturday')
    else:
        print('Sunday')    

IndexDay()


