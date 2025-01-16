import time
from math import sqrt

start_time = time.time()


def power(x):
    digit_list = []
    while x >= 1:
        num = x % 10
        x = x//10
        digit_list.append(num)
    return digit_list


answer_list = []
answer = 0
for i in range(10, 200000):
    for n in power(i):
        answer = n**5+answer
    if answer == i:
        answer_list.append(answer)
        answer = 0
    else:
        answer = 0

print("All the numbers that be written as the sum of fifth powers of their digits is {}".format(
    sum(answer_list)))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
