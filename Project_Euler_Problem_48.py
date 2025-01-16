import time
from math import sqrt

start_time = time.time()

def last_10_digits(x):
    digit_list=[]
    while len (digit_list)<10:
        num=x%10
        x=x//10
        digit_list.append(num)
    digit_list=[i for i in reversed(digit_list)]
    string=int("".join(map(str,digit_list)))
    return string

number=0

for i in range(1,1001):
    number+=i**i

print("last 10 digits of the series is {}".format(last_10_digits(number)))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
