import time
from math import sqrt
import numpy

start_time = time.time()

# triangle = 3
# square = 4
# pentagonal = 5
# hexagonal = 6
# heptagonal = 7
# octagonal = 8


def is_figurate_number(x):
    n1 = (sqrt(1+8*x)-1)/2
    n2 = sqrt(x)
    n3 = (sqrt(1+24*x)+1)/6
    n4 = (sqrt(1+8*x)+1)/4
    n5 = (sqrt(9+40*x)+3)/10
    n6 = (sqrt(1+3*x)+1)/3

    if x == 0:
        return 0
    elif n1 == int(n1):
        return 3
    elif n2 == int(n2):
        return 4
    elif n3 == int(n3):
        return 5
    elif n4 == int(n4):
        return 6
    elif n5 == int(n5):
        return 7
    elif n6 == int(n6):
        return 8
    else:
        return False


def polygonal_numbers(x, y, polygon):
    num_list = []
    if polygon == 3:
        limit1 = round((sqrt(1+8*x)-1)/2)
        limit2 = round((sqrt(1+8*y)-1)/2)
        for n in range(limit1, limit2+1):
            triangle = int(n*(n+1)/2)
            if len(str(triangle)) == len(str(x)):
                num_list.append(triangle)
    elif polygon == 4:
        limit1 = round(sqrt(x))
        limit2 = round(sqrt(y))
        for n in range(limit1, limit2+1):
            square = int(n**2)
            if len(str(square)) == len(str(x)):
                num_list.append(square)
    elif polygon == 5:
        limit1 = round((sqrt(1+24*x)+1)/6)
        limit2 = round((sqrt(1+24*y)+1)/6)
        for n in range(limit1, limit2):
            pentagonal = int(n*(3*n-1)/2)
            if len(str(pentagonal)) == len(str(x)):
                num_list.append(pentagonal)
    elif polygon == 6:
        limit1 = round((sqrt(1+8*x)+1)/4)
        limit2 = round((sqrt(1+8*y)+1)/4)
        for n in range(limit1, limit2+1):
            hexagonal = int(n*(2*n-1))
            if len(str(hexagonal)) == len(str(x)):
                num_list.append(hexagonal)
    elif polygon == 7:
        limit1 = round((sqrt(9+40*x)+3)/10)
        limit2 = round((sqrt(9+40*y)+3)/10)
        for n in range(limit1, limit2+1):
            heptagonal = int(n*(5*n-3)/2)
            if len(str(heptagonal)) == len(str(x)):
                num_list.append(heptagonal)
    elif polygon == 8:
        limit1 = round((sqrt(1+3*x)+1)/3)
        limit2 = round((sqrt(1+3*y)+1)/3)
        for n in range(limit1, limit2):
            octagonal = int(n*(3*n-2))
            if len(str(octagonal)) == len(str(x)):
                num_list.append(octagonal)
    else:
        return
    return num_list


triangle_num_list = polygonal_numbers(1000, 9999, 3)
square_num_list = polygonal_numbers(1000, 9999, 4)
pentagonal_num_list = polygonal_numbers(1000, 9999, 5)
hexagonal_num_list = polygonal_numbers(1000, 9999, 6)
heptagonal_num_list = polygonal_numbers(1000, 9999, 7)
octagonal_num_list = polygonal_numbers(1000, 9999, 8)


polygonal_num_list = [triangle_num_list, square_num_list, pentagonal_num_list,
                      hexagonal_num_list, heptagonal_num_list, octagonal_num_list]


answer_list = []


def answer(x, i, l, y):
    num_list = l.copy()
    num_list.pop(i)
    if num_list == []:
        if str(x)[2:4] == str(y)[0:2]:
            return True
        else:
            return False
    for a in range(0, len(num_list)):
        for n in num_list[a]:
            if str(x)[2:4] == str(n)[0:2]:
                if answer(n, a, num_list, y) == True:
                    answer_list.append(n)
                    return True
                else:
                    continue
    return False


answer_list = []
for i in triangle_num_list:
    answer_list.append(i)
    if answer(i, 0, polygonal_num_list, i) == True:
        break
    else:
        answer_list.remove(i)

print("sum of the only ordered set is {}".format(sum(answer_list)))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
