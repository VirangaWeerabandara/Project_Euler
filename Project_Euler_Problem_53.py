import time
from math import factorial

start_time = time.time()


def digits(x):
    digit_list = []
    while x >= 1:
        num = x % 10
        x = x//10
        digit_list.append(num)
    digit_list.sort()
    return len(digit_list)


values = []

for n in range(1, 101):
    for r in range(1, n):
        f = factorial(n)/(factorial(r)*factorial(n-r))
        if digits(f) >= 7:
            values.append(f)

print("There are {} values of given notation for (1 <= n <= 100) ".format(len(values)))


finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
