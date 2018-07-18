import datetime

now = datetime.datetime.now()

aniversary = datetime.datetime(2012,11,13,16,55)

import time
yesterday= datetime.datetime.fromtimestamp(time.time() - 3600*24)

print(now,aniversary,yesterday)

print(now.strftime("%A %d/%b/%Y %H:%M"))

datestring="12/15/2013 15:30"


date_fmt = "%m/%d/%Y %H:%M"
input_date = datetime.datetime.strptime(datestring,date_fmt)
print(input_date)

next_week = now + datetime.timedelta(days=7)
print(next_week)

for i in range(15):
    print((now+datetime.timedelta(days=i)).strftime("%a"))

import calendar

first_weekday,number_days=calendar.monthrange(2012,2)
print(first_weekday,number_days)

print(calendar.month(2012,2))