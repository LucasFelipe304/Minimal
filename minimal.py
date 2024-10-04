from datetime import datetime, date
import os

# Global constants
DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def get_username():
    """Returns the system's username."""
    return os.getlogin()

def line():
    """Prints a separator line."""
    print("-", * 25)

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
    print("Day information ->", current_day(), daily_info)

