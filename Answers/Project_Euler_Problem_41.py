import time
from math import sqrt

star_time = time.time()


def digits(x):
    digit_list = []
    while x >= 1:
        num = x % 10
        x = x//10
        digit_list.append(num)
    digit_list = [i for i in reversed(digit_list)]
    digit_list1 = list(dict.fromkeys(digit_list))
    digit_list2 = [n for n in digit_list if n != 0 and n != 9 and n != 8]

    if digit_list1 == digit_list2:
        return True
    else:
        return False


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


list1 = []

for i in range(7777777, 10, -2):
    if digits(i) == True and is_prime(i) == True:
        list1.append(i)

print(list1[0])

finish_time = time.time()

duration = finish_time-star_time

print("Programme took {} seconds to finish".format(duration))
