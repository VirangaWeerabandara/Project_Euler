import time
from math import sqrt

start_time = time.time()


def is_prime(number):
    list1 = []

    if number == 1:
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


prime_list = [2, 3, 5, 7]
num_list = [1, 2, 3, 4, 5, 6, 7]


conjecture = True
i = 11
n = 8

while conjecture == True:
    if is_prime(i) == True:
        prime_list.append(i)
        i += 2
        num_list.append(n)
        n += 1
    elif is_prime(i) == False:
        for a in prime_list:
            for b in num_list:
                f = a+2*b**2
                if i < f:
                    break
                if i != f:
                    continue
                if i == f:
                    break
            if i == f:
                break
        if i != f:
            # print(i,f,a,b)
            conjecture = False
            print(
                "The Smallest composite that makes the conjecture false is {} ".format(i))
        i += 2
        num_list.append(n)
        n += 1


finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
