import time
import datetime

start_time = time.time()

def digits(x,y,z):
    digit_list=[]
    list1=[x,y,z]
    for i in list1:     
        while i>=1:
            num=i%10
            i=i//10
            digit_list.append(num)
    digit_list1=digit_list.copy()
    digit_list1=list(dict.fromkeys(digit_list1))
    digit_list1=[y for y in digit_list1 if y != 0]
    return digit_list,digit_list1

# print(digits(372,187,69564))

pandigital_num_list=[]

for i in range(1,1000):
    for n in range(1,1000):
        product=i*n
        condition1=len(digits(i,n,product)[0])
        condition2=len(digits(i,n,product)[1])
        if condition1 == 9 and condition2 == 9:
            #print(i,n,product)
            pandigital_num_list.append(product)

for i in range(1,10):
    for n in range(1,100001):
        product=i*n
        condition1=len(digits(i,n,product)[0])
        condition2=len(digits(i,n,product)[1])
        if condition1 == 9 and condition2 == 9:
            #print(i,n,product)
            pandigital_num_list.append(product)


pandigital_num_list=list(dict.fromkeys(pandigital_num_list))

print(pandigital_num_list)

print(sum(pandigital_num_list))          

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))

