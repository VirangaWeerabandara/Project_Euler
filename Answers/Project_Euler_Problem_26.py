import time
from math import sqrt

start_time = time.time()


def is_prime(number):
    list1 = []
    if number <= 0:
        return False

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

# def prime_factors(x):
#     prime_factor_list=[]
#     if is_prime(x)==True:
#         prime_factor_list.append(1)
#         prime_factor_list.append(x)
#     elif is_prime(x)==False:
#         prime_list=[a for a in range(1,int(sqrt(x)//1)+1) if is_prime(a)==True]
#         for i in prime_list:
#             if x%i==0:
#                 while x%i==0:
#                     x=x/i
#                     prime_factor_list.append(i)
#     #prime_factor_list=list(dict.fromkeys(prime_factor_list))
#     return prime_factor_list


def recurring_cycle(x):
    recurring_list = []
    if x < 10:
        a = 10
    elif x < 100 and x > 10:
        a = 100
    elif x > 100 and x < 1000:
        a = 1000
    a1 = a
    n = 0
    while n != a1:
        c = a//x
        a = (a % x)*a1
        n = a
        recurring_list.append(c)
        if a == 0:
            return(0)
        if a == a1:
            break
        if len(recurring_list) == x:
            recurring_list = list(dict.fromkeys(recurring_list))
            break
    return len(recurring_list)


prime_list = []

for i in range(1, 1001):
    if is_prime(i):
        prime_list.append(i)

len_recurring_cycle_list = []

for a in prime_list:
    len_recurring_cycle_list.append([recurring_cycle(a), a])

print("Value of d is {} and length of this recurring cycle is {}".format(
    max(len_recurring_cycle_list)[1], max(len_recurring_cycle_list)[0]))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
