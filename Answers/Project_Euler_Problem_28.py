import time
from math import sqrt

start_time = time.time()

list1=[]
list2=[3]
list3=[5]
list4=[7]

for a in range(1,1002,2):
    num1=a*a
    list1.append(num1)


constant = 1001*1001  
i=1

while list2[-1]<constant:
    num2=list2[-1] + 2 + 8*i
    list2.append(num2)
    num3=list3[-1] + 4 + 8*i
    list3.append(num3)
    num4=list4[-1] + 6 + 8*i
    list4.append(num4)
    i+=1

list2.remove(list2[-1])
list3.remove(list3[-1])
list4.remove(list4[-1])

answer=sum(list1)+sum(list2)+sum(list3)+sum(list4)

print("Sum of the numbers on the diagonals in a 1001 by 1001 spiral formed is {}".format(answer)) 

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
