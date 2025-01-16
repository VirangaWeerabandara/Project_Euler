import time

start_time=time.time()

number = 2520
i = 2

while i < 21:
    
    if number % i == 0:
        i = i+1
    else:
        i = 2
        number = number+2

print("The smallest positive number that is evenly divisible by all the numbers from 1 to 20 is {}".format(number))

finish_time=time.time()

differnce=finish_time-start_time

print("Code took {} seconds to finish".format(differnce))




