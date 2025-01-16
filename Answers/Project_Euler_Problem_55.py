import time

start_time = time.time()


def is_lychrel(x):
    num = x
    for o in range(50):
        num += int(str(num)[::-1])
        if num == int(str(num)[::-1]):
            return False
    return True


def num_genarator(x):
    y = str(x)[::-1]
    return int(y)


lychrel_num_list = []

for i in range(1, 10001):
    if is_lychrel(i) == True:
        lychrel_num_list.append(i)


print("There are {} Lychrel numbers below 10000".format(len(lychrel_num_list)))


finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))