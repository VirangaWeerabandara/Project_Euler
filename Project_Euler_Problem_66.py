import time
from math import sqrt,isqrt

start_time = time.time()


def convergent(x):
    num1 = 1
    num2 = x[-1]
    for i in range(len(x)-1,0,-1):
        k = num2
        num2 = num2*x[i-1]+num1
        num1 = k
    return [int(num2),int(num1)]


def fundamental_solutions(x):
    if int(sqrt(x))**2 == x:
        return
    else:
        a0 = sqrt(x)//1
        a = a0
        b = 1
        c = 0
        p=1
        q=1
        notation=[int(a0)]
        while p**2-x*q**2!=1:
            c = b*a-c
            b = (x-c**2)/b
            a = int((a0 + c)/b)
            notation.append(int(a))
            p=convergent(notation)[0]
            q=convergent(notation)[1]
    return p,q

ans_list=[]

for n in range(181,1001):   
    if fundamental_solutions(n)!=None:
        ans_list.append([fundamental_solutions(n)[0],n])


print("value of D is {} when value of x is largenst ".format(max(ans_list)[1]))       


finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
