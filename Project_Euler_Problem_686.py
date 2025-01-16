import time
from math import log

start_time = time.time()


def leading_digits(x):
    num=x//10**(int(log(x,10))-2)
    return num


count=1
number=678910
i=90
num_list=[]

# while count<number:
#     num=2**i
#     if leading_digits(num)==123:
#         num_list.append(i)
#         count+=1
#     i+=1

while count<number:
    if leading_digits(2**(i+289))==123:
        count+=1
        i+=289
    elif leading_digits(2**(i+196))==123:
        count+=1
        i+=196
    elif leading_digits(2**(i+485))==123:
        count+=1
        i+=485
    else:
        print("error")
    


print(i)


finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
