import time

start_time = time.time()

f = open("Project Euler Problem 13 Resorces.txt", "r").readlines()

num_list = []

sumOflist = 0

for i in range(0, len(f)):
    num_list.append(f[i].strip())
    sumOflist = sumOflist+int(num_list[i])


print("First 10 digits of the Sum of the given one hundred, 50 digit number is: {}".format(
    str(sumOflist)[0:10]))


finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))

