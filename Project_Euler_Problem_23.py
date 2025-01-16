import time,math

start_time = time.time()

def divisors(number):
    divisors_list = [1]
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            n = number/i
            divisors_list.append(i)
            divisors_list.append(n)
    return sum(dict.fromkeys(divisors_list))

num_list=[]

for i in range(0,28124):
    num_list.append(i)

#print(num_list)

abundant_num_list=[]

for number in range(12,28124):
    if number<divisors(number):
        abundant_num_list.append(number)

# print(abundant_num_list)

# print(len(abundant_num_list))

sum_ab_num_list=[]

for a in range(0,len(abundant_num_list)):
    
    for b in range(0,len(abundant_num_list)):
        num=abundant_num_list[a]+abundant_num_list[b]
        sum_ab_num_list.append(num)
    

print("The sum of all the positive integers whitch can not be written as the sum of two abundant numbers = {}".format(sum(list(set(num_list)-set(abundant_num_list)))))


finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))