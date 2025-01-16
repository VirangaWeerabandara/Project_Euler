import time

start_time = time.time()


def digits(x):
    digit_list=[]
    while len(digit_list)<10:
        num=x%10
        x=x//10
        digit_list.append(num)
    digit_list=[i for i in reversed(digit_list)]
    return digit_list

number=28433*(2)**(7830457)+1

print("last 10 digits of the 2,357,207 digit number is {}".format(digits(number)))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
