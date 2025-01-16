import time
from math import factorial, sqrt


start_time = time.time()


def digits(x):
    digit_list = []
    while x >= 1:
        num = x % 10
        x = x//10
        digit_list.append(num)
    digit_list = [i for i in reversed(digit_list)]
    return digit_list


prime_list = []


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


for i in range(11, 1000000, 2):
    if is_prime(i) == True:
        prime_list.append(i)

circular_prime_list = [2, 3, 5, 7]

for n in prime_list:
    digit_list = digits(n)
    prime_list2 = [n]
    for a in range(0, len(digit_list)-1):
        digit_list = digit_list[1:]+digit_list[:1]
        number = int("".join(map(str, digit_list)))
        if is_prime(number) == True:
            prime_list2.append(number)
            continue
        else:
            break
    if len(digit_list) == len(prime_list2):
        circular_prime_list.append(n)

print("There are {} circular primes bellow one million".format(
    len(circular_prime_list)))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
