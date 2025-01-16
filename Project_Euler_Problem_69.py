import time
from math import sqrt

start_time = time.time()


def is_prime(number):
    list1 = []

    if number == 1:
        return False

    if number == 2 or number == 3 or number == 5 or number == 7:
        return True

    for i in range(2, int(sqrt(number))+1):
        if number % i == 0:
            while number % i == 0:
                number = number/i
                list1.append(i)
                if list1 != []:
                    return False
    if list1 == []:
        return True


n = 1
answer = 2

while answer <= 1000000:
    if answer <= 1000000:
        if is_prime(n) == True:
            answer = answer*n
    n += 2

print("Number with the maximum ratio is {}".format(int(answer/(n-2))))


finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
