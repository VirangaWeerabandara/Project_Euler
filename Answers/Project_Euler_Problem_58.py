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


prime_list = [3, 5, 7]
non_prime_list = [1, 9]

num1 = 3
num2 = 5
num3 = 7

condition = False

i = 1
n = 5

while condition == False:
    num1 = num1 + 2 + 8*i
    if is_prime(num1):
        prime_list.append(num1)
    else:
        non_prime_list.append(num1)
    num2 = num2 + 4 + 8*i
    if is_prime(num2):
        prime_list.append(num2)
    else:
        non_prime_list.append(num2)
    num3 = num3 + 6 + 8*i
    if is_prime(num3):
        prime_list.append(num3)
    else:
        non_prime_list.append(num3)
    non_prime_list.append(n**2)
    i += 1
    n += 2
    f = len(prime_list)/(len(prime_list)+len(non_prime_list))*100
    if f <= 10:
        condition = True

print("side length of spiral is {}".format(i*2+1))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
