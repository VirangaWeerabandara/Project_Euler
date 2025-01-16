import time
from math import sqrt

start_time = time.time()

count = 0

for i in range(2, 10001):
    if int(sqrt(i))**2 != i:
        a0 = sqrt(i)//1
        a = a0
        b = 1
        c = 0
        period = 0
        while a != 2*a0:
            c = b*a-c
            b = (i-c**2)/b
            a = int((a0 + c)/b)
            period += 1
        # print(i,period)
    if period % 2 == 1:
        count += 1

print("There are {} odd periods ".format(count))

finish_time = time.time()

differnce = finish_time-start_time

print("Code took {} seconds to finish".format(differnce))
