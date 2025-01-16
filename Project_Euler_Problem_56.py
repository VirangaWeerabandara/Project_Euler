import time

start_time = time.time()


def digit_sum(x):
    digit_list=[]
    while x>=1:
        num=x%10
        x=x//10
        digit_list.append(num)
    return sum(digit_list)

sum_list=[]

for a in range(1,101):
    for b in range(1,101):
        number=a**b
        sum_list.append(digit_sum(number))

print(max(sum_list))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
