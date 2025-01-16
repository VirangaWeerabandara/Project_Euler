import time
from math import sqrt
from itertools import permutations

start_time = time.time()


def digits(x):
    digit_list = []
    while x >= 1:
        num = x % 10
        x = x//10
        digit_list.append(num)
    digit_list = [i for i in reversed(digit_list)]
    digit_list = digit_list[0:-1][1:]+digit_list[0:-1][:1]+digit_list[-1:]
    a = int("".join(map(str, digit_list)))
    digit_list = digit_list[0:-1][1:]+digit_list[0:-1][:1]+digit_list[-1:]
    b = int("".join(map(str, digit_list)))
    return a, b

# print(digits(1487))


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


# print(digits(1568))
prime_list = []
parameters = [[1111, 1999], [2111, 2999], [3111, 3999], [4111, 4999], [
    5111, 5999], [6111, 6999], [7111, 7999], [8111, 8999], [9111, 9999]]

for a, b in parameters:
    for i in range(a, b+1):
        if is_prime(i) == True:
            prime_list.append(i)

prime_list.remove(1487)

for n in prime_list:
    num1 = digits(n)
    if is_prime(num1[0]) == True and is_prime(num1[1]) == True:
        if num1[0] != num1[1]:
            if num1[0] > num1[1]:
                ans1 = num1[0]-num1[1]
                ans2 = num1[1]-n
                if ans1 == ans2:
                    break

            elif num1[0] < num1[1]:
                ans1 = num1[1]-num1[0]
                ans2 = num1[0]-n
                if ans1 == ans2:
                    break

number = int(str(n)+str(num1[0])+str(num1[1]))

print("{} is the 12-digit number formed by concatenating the three terms in the sequence".format(number))

finish_time = time.time()

differnce = finish_time-start_time

print("Code took {} seconds to finish".format(differnce))
