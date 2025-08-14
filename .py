import calendar

year = int(input("Enter the year : "))

cal = calendar.TextCalendar(calendar.SUNDAY)

for month in range (1,13):
    print(cal.formatmonth(year,month))