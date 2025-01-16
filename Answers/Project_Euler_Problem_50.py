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


prime_list = [2, 3, 5, 7]
i = 11

while sum(prime_list) <= 1000000:
    if is_prime(i) == True:
        prime_list.append(i)
    i += 2

# print(len(prime_list))
# print(sum(prime_list))
prime_list.remove(prime_list[-1])

while sum(prime_list) < 1000000:
    prime_list.remove(prime_list[0])
    if(sum(prime_list) < 1000000 and is_prime(sum(prime_list)) == True):
        break


print("Answer is {}".format(sum(prime_list)))
# print(len(prime_list))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
