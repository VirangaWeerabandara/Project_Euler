import time
from math import sqrt

start_time = time.time()


def is_pentagonal(x):
    f=(1 + sqrt(1+24*x))/6
    if int(f)==f:
        return True
    else:
        return False

answer=False
n=1

while answer==False:
    f1=n*(3*n-1)/2
    for i in range(1,n):
        f2=i*(3*i-1)/2
        sum=f1+f2
        difference=f1-f2
        if is_pentagonal(sum)==True and is_pentagonal(difference)==True:
            print("minimum value of D is {}".format(int(difference)))
            answer=True
            break
    n+=1        


finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))

