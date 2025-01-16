import time
import math

start_time = time.time()


def divisors(number):
    divisors_list = [1]
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            n = number/i
            divisors_list.append(i)
            divisors_list.append(n)
    return sum(divisors_list)


amicable_num_list = []


for i in range(9, 10000):
    if i != divisors(i):
        if i == divisors(divisors(i)):
            amicable_num_list.append(i)


print("Sum of the Amicable numbers under 10000 is: {}".format(sum(amicable_num_list)))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
