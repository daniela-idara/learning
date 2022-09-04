#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#


# TODO: import the calendar module
import calendar
import os

# TODO: create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
# str = c.formatmonth(2022, 1, 0, 0)
# print(str)

# TODO: create an HTML formatted calendar
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# str = hc.formatmonth(2022, 1)
# print(str)

## printing this to a new file so I can view the HTML file in browser
# os.mkdir("HTML")
# newfile = open("HTML/calendar.html", "w+") # make file
# newfile.write(str)

# TODO: loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
# for i in c.itermonthdays(2022, 1):
#     print(i)
  
# TODO: The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
# for name in calendar.month_name:
#     print(name)

# for day in calendar.day_name:
#     print(day)

# TODO: Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:

print("Team meetings will be on:")

for m in range(1,13): # this range is the months of the year
    cal = calendar.monthcalendar(2022, m)
    weekone = cal[0]
    weektwo = cal[1]
    if weekone[calendar.FRIDAY] != 0: # if week one's friday is not a 0
        meetday = weekone[calendar.FRIDAY] # we meet
    else: # if it is a 0
        meetday = weektwo[calendar.FRIDAY] # we meet the in week 2 of the month
    print(calendar.month_name[m], meetday) 