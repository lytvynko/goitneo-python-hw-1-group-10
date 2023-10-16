from datetime import datetime, timedelta, date
from collections import defaultdict 

def get_birthdays_week(users):
  birthdays_week = defaultdict(list)
  current_date = datetime.today().date()
  
  for user in users:
    name = user["name"]
    birthday = user["birthday"].date()
    birthday_this_year = birthday.replace(year=current_date.year)
    days_difference = (birthday_this_year - current_date).days
    day_of_week = (current_date + timedelta(days=days_difference)).strftime("%A")
    
    if days_difference >= 0 and days_difference < 7:
      birthdays_week[day_of_week].append(name)

  for day, names in birthdays_week.items():
    print(f"This week don't forget to wish your collegues a happy birthday. On {day}: {', '.join(names)}")

# For tests

# users = [
#     {"name": "Test1 Test1", "birthday": datetime(1955, 10, 18)},
#     {"name": "Test2 Test2", "birthday": datetime(1980, 10, 22)},
#     {"name": "Test3 Test3", "birthday": datetime(1964, 10, 29)},
# ]

# get_birthdays_week(users)