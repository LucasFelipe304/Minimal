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

current_day = date.today()
print(current_day)
