import time
from math import log

start_time = time.time()

data = open("Project Euler Problem 99 Resorces.txt", "r").readlines()

num_list = []
num=0
answer=0

for i in data:
    new_list=[int(x) for x in i.split(",")]
    num_list.append(new_list)

for j in range(0,len(num_list)):
    number=num_list[j][1]*log(num_list[j][0])
    if number>num:
        num=number
        answer=j+1


print("{} is the line number that has the greatest numerical value".format(answer))


finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
