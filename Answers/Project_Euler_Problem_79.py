import time
from math import sqrt

start_time = time.time()


num_list=open("Project Euler Problem 79 Resorces.txt","r").readlines()

data_list=[]

for i in range(0,len(num_list)):
    data_list.append(int(num_list[i].strip()))

data_list=dict.fromkeys(data_list)




finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
