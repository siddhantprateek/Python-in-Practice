import calendar
# CALENDER
# IMPORT CALENDER

# MONTH (<YEAR>, <MONTH>, <HORIZONTAL GAPS BETWEEN DATES OR SIZE OF CALENDER>, <VERTICAL SPACES>)
cal = calendar.month(2016, 2, 5, 2)
print("Here is the calendar:")
print(cal)


m = calendar.firstweekday()
print(m)

leap_year = calendar.isleap(2010)
print(leap_year)
