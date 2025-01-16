import time

start_time = time.time()

num_list = []

for a in range(2, 101):
    for b in range(2, 101):
        number = a**b
        num_list.append(number)


num_list=list(dict.fromkeys(num_list))

print("There are {} distict terms in the given sequence".format(len(num_list)))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
