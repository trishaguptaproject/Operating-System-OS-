#3e. Write a python code to develop calendar module.
import calendar

def show_full_year_calendar(year):
    print(f"\nFull Calendar for {year}:\n")
    print(calendar.calendar(year))

def show_month_calendar(year, month):
    print(f"\nCalendar for {calendar.month_name[month]} {year}:\n")
    print(calendar.month(year, month))

def is_leap_year(year):
    if calendar.isleap(year):
        print(f"\n{year} is a leap year.")
    else:
        print(f"\n{year} is not a leap year.")

print("Calendar Module")

# Ask user for year
year = int(input("Enter the year: "))

# Display full year calendar
show_full_year_calendar(year)

# Ask for a specific month
month = int(input("\nEnter the month number (1-12) to view that month's calendar: "))

# Display month calendar
show_month_calendar(year, month)

# Check if the year is a leap year
is_leap_year(year)
