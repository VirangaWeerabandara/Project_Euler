import time
from math import sqrt

start_time = time.time()

prime_list = [2, 3, 5, 7]
number = 11


def is_prime(number):
    list1 = []

    if number == 1 or number == 0:
        return False

    for i in range(2, int(sqrt(number))+1):
        if number % i == 0:
            while number % i == 0:
                number = number/i
                list1.append(i)
                if list1 != []:
                    return False
    if list1 == []:
        return True


end_number = 2000000

while number <= end_number:
    if is_prime(number) == True:
        prime_list.append(number)
    number += 2


print("sum of all the prime numbers below two million is {}".format(sum(prime_list)))


finish_time = time.time()

differnce = finish_time-start_time

print("Code took {} seconds to finish".format(differnce))
