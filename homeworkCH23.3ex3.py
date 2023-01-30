from datetime import datetime

date_string = input("Please, enter the date in the specified format YYYY-MM-DD")

try:
    user_date = datetime.strptime(date_string, "%Y-%m-%d")
    print(user_date.strftime("%A"))
except ValueError:
    print("The format of the date entered is not correct")
