import time
from math import factorial, sqrt


start_time = time.time()


def digits(x):
    digit_list = []
    while x >= 1:
        num = x % 10
        x = x//10
        digit_list.append(num)
    return digit_list


def is_palindrome(n):

    digit_list = digits(n)
    digit_list1 = [i for i in reversed(digit_list)]
    if digit_list1[0] == 0:
        return False
    if digit_list == digit_list1:
        return True
    else:
        return False


def binary_num(y):
    binary_digit_list = []
    while y >= 1:
        num = y % 2
        y = y//2
        binary_digit_list.append(num)
    binary_digit_list = [i for i in reversed(binary_digit_list)]
    bin_number = int("".join(map(str, binary_digit_list)))
    return bin_number


dubble_base_palindrome_num_list = []

for i in range(1, 1000000):
    bin_num_i = binary_num(i)
    if is_palindrome(i) == True and is_palindrome(bin_num_i) == True:
        dubble_base_palindrome_num_list.append(i)

print("Sum of all the numbers, less than one million, which are palindromic in base 10 and base 2 is {}".format(
    sum(dubble_base_palindrome_num_list)))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
