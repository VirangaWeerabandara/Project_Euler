import time
import datetime

start_time = time.time()


def weekday_name(x):
    days1 = datetime.datetime.strptime(x, "%Y-%m-%d").weekday()
    days2 = datetime.datetime.strptime(x, "%Y-%m-%d").date().day
    return days1, days2


start_day = datetime.datetime(1901, 1, 1).date()
end_date = datetime.datetime(2001, 1, 1).date()

n = 1
sunday_list = []


while start_day != end_date:
    start_day = start_day + datetime.timedelta(n)
    if list(weekday_name(str(start_day)))[1] == 1 and list(weekday_name(str(start_day)))[0] == 6:
        sunday_list.append(start_day)

print("There are {} sundays fell on the first month of the twntieth century".format(len(sunday_list)))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
