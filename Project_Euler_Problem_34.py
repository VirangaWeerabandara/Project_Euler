import time
from math import factorial

start_time = time.time()


def digits(x):
    digit_list = []
    while x >= 1:
        num = x % 10
        x = x//10
        digit_list.append(num)
    return digit_list


num = 0

for i in range(1, 10):
    num = num + factorial(9)

#print(num)

answer_list = []

for n in range(24, num+1):
    answer = 0
    for x in digits(n):
        answer += factorial(x)
    if answer == n:
        answer_list.append(n)


print("All the numbers which are equal to the sum of the factorial of their digits is {}".format(
    sum(answer_list)))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
