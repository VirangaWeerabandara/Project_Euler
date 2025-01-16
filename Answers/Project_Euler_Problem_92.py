import time

start_time = time.time()


def digit_square(x):
    sum = 0
    for i in str(x):
        sum += int(i)**2
    return sum


list1 = [False]*10000001


for i, n in enumerate(list1):
    if n == True:
        continue
    if i == 0 or i == 1:
        continue
    if i == 89:
        list1[i] = True
    num = i
    num_list = []
    while num != 89:
        if num == 1:
            num_list = []
            break
        num = digit_square(num)
        if num == 89:
            list1[i] = True
        else:
            num_list.append(num)
    # for a in num_list:
    #     list1[a] = True


print("{} starting numbers will arrive at 89".format(list1.count(True)))


finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
