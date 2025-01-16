import time
from math import sqrt


start_time = time.time()

t = 41041
n = 287

while t >= 40755:
    pf = (1+sqrt(1+24*t))/6
    if pf == int(pf):
        hf = (1+sqrt(1+8*t))/4
        if hf == int(hf):
            print(
                "Next Triangle number that is both a pentagon and hexogon number is {}".format(int(t)))
            break
    t = n*(n+1)/2
    n += 1


finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
