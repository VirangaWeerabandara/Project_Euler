import time
from math import sqrt

start_time = time.time()


def factors(x):
    factor_list = []
    for i in range(2, int(sqrt(x)//1)+1):
        if is_prime(x) == False:
            if x % i == 0:
                while x % i == 0:
                    x = x/i
                    factor_list.append(i)
        elif is_prime(x) == True:
            factor_list.append(x)
            break
    factor_list = list(dict.fromkeys(factor_list))
    return factor_list

# print(factors(10000))


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


n = 1000
answer = False

while answer == False:
    if is_prime(n) == False:
        list1 = factors(n)
        list2 = factors(n+1)
        list3 = factors(n+2)
        list4 = factors(n+3)
        if len(list1) == len(list2) == len(list3) == len(list4) == 4:
            print(n)
            answer = True
    n += 1


finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
