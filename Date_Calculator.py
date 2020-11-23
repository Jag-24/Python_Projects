from datetime import date, timedelta, datetime


First_date = input("Please enter first date in format (YYYYMMDD): ")
First_date = datetime(year = int(First_date[0:4]), month = int(First_date[4:6]), day = int(First_date[6:8]))
Second_date = input("Please enter second date in format (YYYYMMDD): ")
Second_date = datetime(year = int(Second_date[0:4]), month = int(Second_date[4:6]), day = int(Second_date[6:8]))

delta = Second_date - First_date
print("Days until Second date:")
print(delta.days)
