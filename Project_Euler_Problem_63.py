import time
from math import sqrt

start_time = time.time()


def digits(x):
    x = str(x)
    return len(x)


answer_list = []
count = 0


for i in range(1, 10):
    n = 1
    f = 1
    answer = False
    while answer == False:
        f = i**n
        if digits(f) == n:
            count += 1
            n += 1
        else:
            answer = True


print("there are {} n-digit positive integers exist which are also an nth power".format(count))

finish_time = time.time()

differnce = finish_time-start_time

print("Code took {} seconds to finish".format(differnce))
