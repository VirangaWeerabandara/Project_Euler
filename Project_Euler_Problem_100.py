import time

start_time = time.time()


num1 = 15
num2 = 21
parameter = 1000000000000
status = False

while status == False:
    x = 3*num1 + 2*num2 - 2
    y = 4*num1 + 3*num2 - 3
    num1 = x
    num2 = y
    if num2 > parameter:
        status = True

print("There are {} blue disks in the box which contain over 10^12 disks".format(num1))


finish_time = time.time()

differnce = finish_time-start_time

print("Code took {} seconds to finish".format(differnce))
