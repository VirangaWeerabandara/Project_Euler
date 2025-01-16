import time
from math import sqrt

start_time = time.time()

x = 101010101
y = 138902663

for a in range(y, x, -2):
    number = (a*10)**2
    new_num = ""
    for b in range(0, 19, 2):
        new_num += str(number)[b]
    if int(new_num) == 1234567890:
        print("{} is the unique integer whose square has the given form".format(a*10))
        break


finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
