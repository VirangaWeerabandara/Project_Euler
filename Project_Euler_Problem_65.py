import time
from math import sqrt
from fractions import Fraction

start_time = time.time()


digit_list = [2, 1]
n = 2

while len(digit_list) < 100:
    digit_list.append(n)
    digit_list.append(1)
    digit_list.append(1)
    n += 2

digit_list.pop(100)
num1 = 1
num2 = 1
for i in range(99, 0, -1):
    k = num2
    num2 = num2*digit_list[i-1]+num1
    num1 = k
new_list = list(str(num2))
answer = 0

for a in new_list:
    answer += int(a)

print("sum of the digits in the numerator of 100th convergent is {} ".format(answer))

finish_time = time.time()

differnce = finish_time-start_time

print("Code took {} seconds to finish".format(differnce))
