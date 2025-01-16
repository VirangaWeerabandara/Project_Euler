import time
from math import sqrt

start_time = time.time()

p = 0
p_list = []

while p <= 1000:
    for a in range(3, 1000):
        for b in range(a+1, 1000):
            c = sqrt(a**2+b**2)
            if c == float(c//1):
                p = a+b+int(c)
                if p >= 1000:
                    break
                p_list.append(p)

new_p_list = list(dict.fromkeys(p_list))
count_list = []

for i in new_p_list:
    count_list.append([p_list.count(i), i])

print("maximum of p is {}".format(max(count_list)[1]))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))


# # # l=[1,2,3,4,5,6,7]

# # # a=11

# # # if a not in l:
# # #     print(True)
# # # else:
# # #     print(False)

