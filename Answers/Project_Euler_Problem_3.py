import math,time
start_time=time.time()

number = 600851475143
# 600851475143

number2=int(math.sqrt(number))

newlist=[]
for i in range(2,number2):
    if number%i ==0:
        while number%i==0:
            number=number/i
            #print(i)
            newlist.append(i)

print(newlist)

print("largest prime factor of the number is {}".format(newlist[-1]))
finish_time=time.time()


differnce=finish_time-start_time

print("Code took {} seconds to finish".format(differnce))




