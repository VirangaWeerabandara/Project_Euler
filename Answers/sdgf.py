import time
from math import sqrt

start_time=time.time()

def is_prime(number):
    list1 = []
    
    if number<=0:
        return False

    if number==1:
        return False

    for i in range(2, int(sqrt(number))+1):
        if number % i == 0:
            while number % i == 0:
                number = number/i
                list1.append(i)
                if list1!=[]:
                    return False
    if list1==[]:
        return True

# list1=[]
# for i in range(2,2000001):
#     list1.append(i)
# start_time=time.time()
# list1=[n for n in list1 if is_prime(n)==True]

# print(sum(list1))

l=[]
for i in range(-1000,1000):
    if is_prime(i)==True:
        l.append(i)

print(l)

end_time=time.time()
diff=end_time-start_time
print(diff)