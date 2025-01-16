import time
from math import sqrt

start_time = time.time()


number = 3/7
num=0
status=False

num_list=[]

while status==False:
    for i in range(999999,0,-1):
        a=int((i*43/100)//1)
        for n in range(a,1,-1):
            num=n/i
            if num<number:
                num_list.append(n)
                break
                




finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))

# print(int(999999*43/100)//1)