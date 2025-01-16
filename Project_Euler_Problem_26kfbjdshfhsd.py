from math import factorial
from math import sin,cos,tan,sqrt

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


print((10**2020+1)**5)