import time

start_time = time.time()

def function(x, y):
    f = x*2+y
    return f


data_list = [[3, 2], [7, 5]]

for i in range(1, 999):
    num1 = function(data_list[i][0], data_list[i-1][0])
    num2 = function(data_list[i][1], data_list[i-1][1])
    data_list.append([num1, num2])

count = 0

for a, b in data_list:
    len1 = len(str(a))
    len2 = len(str(b))
    if len1 > len2:
        count += 1

print("There are {} fractions contain a numerator with more digits than the denominator".format(count))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))