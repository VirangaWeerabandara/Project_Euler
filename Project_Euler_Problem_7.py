import time
from math import sqrt

start_time = time.time()

prime_list = [2,3,5,7]
number = 11


def is_prime(number):
    list1 = []
    if number<=0:
        return False

    if number==1:
        return False

    for i in range(2, int(sqrt(number))+1):
        if number % i == 0:
            while number % i == 0:
                number = number/i
                list1.append(i)
                if list1!=[]:
                    return False
    if list1==[]:
        return True


while len(prime_list) < 10002:
    if is_prime(number) == True:
        #print("it is a prime number")
        prime_list.append(number)
    number = number + 2



# print(prime_list[-1])
# print(prime_list.index(prime_list[-1]))

print("10001 prime number is {}".format(prime_list[10000]))
#print(prime_list)

print(is_prime(7))

finish_time = time.time()

differnce = finish_time-start_time

print("Code took {} seconds to finish".format(differnce))
