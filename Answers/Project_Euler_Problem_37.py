import time
from math import factorial, sqrt


start_time = time.time()


def is_prime(number):
    list1 = []

    if number == 1 or number == 0:
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

def digits(x):
    digit_list=[]
    while x>=1:
        num=x%10
        x=x//10
        digit_list.append(num)

    digit_list=[i for i in reversed(digit_list)]
    return(digit_list) 

def remove_digit_RtoL(y):
    new_list=y
    length=len(new_list)
    dig_list=[]

    while len(new_list)>1:
        del new_list[-1]
        number=int("".join(map(str,new_list)))
        
        if is_prime(number)==True:
            dig_list.append(number)    
            continue
        else:
            return False
    if len(dig_list)==length-1:
        return True

def remove_digit_LtoR(y):
    new_list=y
    length=len(new_list)
    dig_list=[]

    while len(new_list)>1:
        del new_list[0]
        number=int("".join(map(str,new_list)))
        
        if is_prime(number)==True:
            dig_list.append(number)    
            continue
        else:
            return False
    if len(dig_list)==length-1:
        return True


prime_list=[]
n=11

while len(prime_list)<=10:
    if is_prime(n)== True and remove_digit_RtoL(digits(n))==True and remove_digit_LtoR(digits(n))==True:
        prime_list.append(n)
        #print(n)
    n=n+2

print("Sum of the only eleven primes that are both truncatable from left to right and right to left is {}".format(sum(prime_list)))
#print(prime_list)

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
