import time

start_time = time.time()


def digits(x):
    digit_list = []
    while x >= 1:
        num = x % 10
        x = x//10
        digit_list.append(num)
    digit_list.sort()
    return digit_list


k = 0
a = 5
b = 16

while k == 0:
    for i in range(a, b+1):
        x2 = 2*i
        x3 = 3*i
        x4 = 4*i
        x5 = 5*i
        x6 = 6*i
        if digits(x2) == digits(x3) == digits(x4) == digits(x5) == digits(x6):
            print(
                "smallest positive integer,x such that 2x,3x,4x,5x,6x contain the same digits is {}".format(i))
            break
    if digits(x2) == digits(x3) == digits(x4) == digits(x5) == digits(x6):
        break
    a = a*10
    b = int(str(b)+"6")


finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
