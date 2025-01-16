import time
from math import sqrt

start_time = time.time()


def is_prime(number):
    prime_list = []

    if number == 1 or number == 0:
        return False

    if number < 0:
        return False

    for i in range(2, int(sqrt(number)//1)+1):
        if number % i == 0:
            while number % i == 0:
                number = number/i
                prime_list.append(i)
                if prime_list != []:
                    return False
    if prime_list == []:
        return True


a_list = []
b_list = [2]

for i in range(-999, 1000, 2):
    if is_prime(i) == True:
        b_list.append(i)
    if i % 2 == 1:
        a_list.append(i)

max_count = 0

for a in a_list:
    for b in b_list:
        answer = True
        n = 0
        count = 0
        while answer == True:
            f = n**2+a*n+b
            if is_prime(f) == True:
                count += 1
            else:
                answer = False
            n += 1
        if max_count < count:
            max_count = count
            ans = a*b
        elif max_count > count:
            continue

print("coefficients of a and b is {}".format(ans))


finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
