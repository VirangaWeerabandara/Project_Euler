import time
from math import sqrt

start_time = time.time()


def is_prime(number):
    list1 = []

    if number == 1:
        return False

    if number == 2 or number == 3 or number == 5 or number == 7:
        return True

    for i in range(2, int(sqrt(number))+1):
        if number % i == 0:
            while number % i == 0:
                number = number/i
                list1.append(i)
                if list1 != []:
                    return False
    if list1 == []:
        return True


def is_8_primeFamily(x, y):
    if len(str(x)) == 2 or len(str(x)) == 3 or len(str(x)) == 4 or len(str(x)) == 5:
        return False
    digit_list = list(str(x))
    num_list = []
    if y == 0:
        l = 1
    elif y == 1:
        l = 2
    elif y == 2:
        l = 3
    for i in range(l, 10):
        new_list = [str(i) if z == str(y) else z for z in digit_list]
        number = "".join(map(str, new_list))
        if is_prime(int(number)) == True:
            num_list.append(True)

    if len(num_list) == 7:
        return True
    else:
        return False


def pattern_genarator(x, i):
    num_list = []
    if len(str(x)) == 5:
        a1 = int(str(i)+str(i)+str(i)+str(x)[3:5])
        a2 = int(str(i)+str(x)[1]+str(i)+str(i)+str(x)[4])
        a3 = int(str(i)+str(i)+str(x)[2]+str(i)+str(x)[4])
        a4 = int(str(x)[0]+str(i)+str(i)+str(i)+str(x)[4])
        num_list.append(a1)
        num_list.append(a2)
        num_list.append(a3)
        num_list.append(a4)

    elif len(str(x)) == 6:
        b1 = int(str(x)[0:2]+str(i)+str(i)+str(i)+str(x)[5])
        b2 = int(str(x)[0]+str(i)+str(x)[2]+str(i)+str(i)+str(x)[5])
        b3 = int(str(x)[0]+str(i)+str(i)+str(x)[3]+str(i)+str(x)[5])
        b4 = int(str(x)[0]+str(i)+str(i)+str(i)+str(x)[4:6])
        b5 = int(str(i)+str(x)[1:3]+str(i)+str(i)+str(x)[5])
        b6 = int(str(i)+str(x)[1]+str(i)+str(i)+str(x)[4:6])
        b7 = int(str(i)+str(x)[1]+str(i)+str(x)[3]+str(i)+str(x)[5])
        b8 = int(str(i)+str(i)+str(x)[2:4]+str(i)+str(x)[5])
        b9 = int(str(i)+str(i)+str(x)[2]+str(i)+str(x)[4:6])
        b10 = int(str(i)+str(i)+str(i)+str(x)[3:6])
        num_list.append(b1)
        num_list.append(b2)
        num_list.append(b3)
        num_list.append(b4)
        num_list.append(b5)
        num_list.append(b6)
        num_list.append(b7)
        num_list.append(b8)
        num_list.append(b9)
        num_list.append(b10)
    return num_list


for i in range(100000, 999999):
    for a in range(0, 3):
        pattern_list = pattern_genarator(i, a)
        for n in pattern_list:
            if is_prime(n) == True and is_8_primeFamily(n, a) == True:
                print("Smallest prime of the eight prime family is {}".format(n))
                break
        if is_prime(n) == True and is_8_primeFamily(n, a) == True:
            break
    if is_prime(n) == True and is_8_primeFamily(n, a) == True:
        break


finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
