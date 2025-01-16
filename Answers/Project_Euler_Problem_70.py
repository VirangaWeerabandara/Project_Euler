import time
from math import sqrt,prod

start_time=time.time()

end=10000000

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


min_ratio=None
answer=None

prime_list=[]

for i in range(2000,4000):
    if is_prime(i)==True:
        prime_list.append(i)

for i in range(0,len(prime_list)):
    for n in range(i+1,len(prime_list)):
        num1=(prime_list[i]-1)*(prime_list[n]-1)
        num2=prime_list[i]*prime_list[n]
        if num2<end:
            if sorted(str(num1))==sorted(str(num2)):
                # print(num1,num2)
                ratio=num2/float(num1)
                if min_ratio is None or min_ratio>ratio:
                    min_ratio=ratio
                    answer=num2
            else:
                continue 
    
print("Project Euler Answer for the Problem 70 is {}".format(answer))


end_time=time.time()

duration=end_time-start_time

print("Programme took {} seconds to finish".format(duration))

