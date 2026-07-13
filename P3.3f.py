#3f. Write a python code to compare two dates.
from datetime import datetime

# Step 1: Take two dates as input from the user
date_str1 = input("Enter the first date (YYYY-MM-DD): ")
date_str2 = input("Enter the second date (YYYY-MM-DD): ")

# Step 2: Convert strings to datetime objects
date1 = datetime.strptime(date_str1, "%Y-%m-%d")
date2 = datetime.strptime(date_str2, "%Y-%m-%d")

# Step 3: Compare the two dates
if date1 < date2:
    print(f"{date_str1} is earlier than {date_str2}.")
elif date1 > date2:
    print(f"{date_str1} is later than {date_str2}.")
else:
    print("Both dates are the same.")
