import time
from math import sqrt

start_time = time.time()


def is_prime(number):
    list1 = []
    if number <= 0:
        return False

    if number == 1 or number == 4 or number == 6 or number == 8:
        return False

    if number == 2 or number == 3 or number == 5 or number == 7:
        return True

    for i in range(2, int(sqrt(number))+1):
        if number % i == 0:
            while number % i == 0:
                number = number/i
                list1.append(i)
                if list1 != []:
                    return False
    if list1 == []:
        return True


def is_prime_pair(x, y):
    num1 = int(str(x)+str(y))
    num2 = int(str(y)+str(x))
    if is_prime(num1) == True and is_prime(num2) == True:
        return True
    else:
        return False


prime_list = []

for i in range(1, 10000, 2):
    if is_prime(i) == True:
        prime_list.append(i)

answer_list = []
status = False
for a in prime_list:
    for b in reversed(prime_list):
        if is_prime_pair(a, b) == True:
            for c in reversed(prime_list):
                if is_prime_pair(a, c) == True and is_prime_pair(b, c) == True:
                    for d in reversed(prime_list):
                        if is_prime_pair(a, d) == True and is_prime_pair(b, d) == True and is_prime_pair(c, d) == True:
                            for e in reversed(prime_list):
                                if is_prime_pair(a, e) == True and is_prime_pair(b, e) == True and is_prime_pair(c, e) == True and is_prime_pair(d, e) == True:
                                    answer_list.append([a, b, c, d, e])
                                    status = True
                                    break
                        if status == True:
                            break
                if status == True:
                    break
        if status == True:
            break
    if status == True:
        break


print("lowerst sum is {}".format((sum(answer_list[0]))))


# print(is_prime_pair(3,7),is_prime_pair(3,109),is_prime_pair(3,673),is_prime_pair(109,7),is_prime_pair(673,7),is_prime_pair(673,109))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
