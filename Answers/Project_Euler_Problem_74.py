import time
from math import factorial

start_time = time.time()


def digit_factorial(x):
    digit_list = list(str(x))
    number = 0
    for n in digit_list:
        number += factorial(int(n))
    return number


def chain_len(x):
    if digit_factorial(x) == 1 or digit_factorial(x) == 2 or digit_factorial(x) == 10:
        return 1
    num_list = [x]
    number = x
    answer = False
    while answer == False:
        number = digit_factorial(number)
        num_list.append(number)
        # if number==169:
        #     num_list.append(363601)
        #     num_list.append(1454)
        # if number==871:
        #     num_list.append(45361)
        # if number==872:
        #     num_list.append(45362)
        if number == 145 or number == 169 or number == 871 or number == 872 or number == 2 or number == 40585 or number == 363601 or number == 1454 or number == 45361 or number == 45362:
            answer = True
    len_list = len(num_list)
    if number == 169 or number == 1454 or number == 363601:
        len_list += 2
    elif number == 871 or number == 872 or number == 45361 or number == 45362:
        len_list += 1
    return len_list


count_chain = 0

for i in range(1, 1000000):
    if chain_len(i) == 60:
        count_chain += 1

print(count_chain)


end_time = time.time()

difference = end_time-start_time

print("Code took {} seconds to execute".format(difference))
