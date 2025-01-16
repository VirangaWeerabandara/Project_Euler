import time
from math import sqrt

start_time = time.time()


def digits(x):
    digit_list = []
    while x >= 1:
        num = x % 10
        x = x//10
        digit_list.append(num)
    digit_list = [i for i in reversed(digit_list)]
    return digit_list


num_list = []

for i in range(978, 10000):
    list1 = digits(i)
    list2 = [n for n in list1 if n != 0]
    list2 = list(dict.fromkeys(list2))
    if list1 == list2:
        new_list = []
        a = 1
        while len(new_list) < 9:
            number = a*i
            new_list = new_list+digits(number)
            a += 1
            number = 0
        if len(new_list) == 9:
            new_list = list(dict.fromkeys(new_list))
            new_list = [b for b in new_list if b != 0]
            if len(new_list) == 9:
                num = int("".join(map(str, new_list)))
                # print(i,num)
                num_list.append(num)


print("{} is the largest 1 to 9 pandigital number".format(max(num_list)))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
