
# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar
from curses.ascii import isalpha
from datetime import date
from datetime import time
from datetime import datetime

# Counts number of weekday in a year and month
# Handles invalid input errors

def countdays(selYr, selMo, selDay):
            daycount = 0
            weekslist = calendar.monthcalendar(selYr, selMo)
            for week in weekslist:
                if week[selDay] != 0:
                    daycount += 1
            return daycount

print("--Day counter program--\n\nWhich day of the week do you want to count?\n")

run = True
while(run):
    try:

# for day in calendar.day_name:                      # this prints the day, but not the index
#    print(day)                                      # tried .weekday() to get weekday number, but it wouldn't work

        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

        for i,d in enumerate(days):                       # i is the index number
            print (str(i)+":", d)                         # this allows me to print list index + list item

        print("Or 'exit' to quit\n")

       
        selDay = int(input("Enter day by number: "))
        
        if selDay == "exit":
            break
        selDay = int(selDay)

        #if selDay != int:
         #   print ("Invalid selection")
          #  selDay = input("Enter day by number: ")
           # selDay = int(selDay)

        

        while selDay > 6:
            print ("Invalid selection. Select 0 - 6")
            selDay = input("Enter day by number: ")
            selDay = int(selDay)

        if selDay <= 6: 
            selYr = input("Enter year: ")
            selYr = int(selYr)
            selMo = input("Enter month by number: ")
            selMo = int(selMo) 

        while selMo > 12:
            print ("Invalid selection. Select 0 - 12")
            selMo = input("Enter month by number: ")
            selMo = int(selMo)  
        print("\nYou want to know how many", calendar.day_name[selDay]+"s exist in", calendar.month_name[selMo], selYr)

        # c = calendar.TextCalendar(calendar.SUNDAY)
        # str = c.formatmonth(selYr, selMo, 0, 0)
        # print("\n",str)

        # for selMo in range(1,13):
        #     cal = calendar.monthcalendar(selYr, selMo)
        #     print(cal)


        total = countdays(selYr, selMo, selDay)

        print("\nThere are", total, calendar.day_name[selDay]+"s in the month and year specified\n---------")
    except Exception as e:
        print(e)
        print("Sorry, that's not valid input")


