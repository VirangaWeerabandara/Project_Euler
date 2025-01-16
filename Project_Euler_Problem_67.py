import time

start_time = time.time()

data = open("Project Euler Problem 67 Resorces.txt", "r").readlines()


num_list = []


for i in range(0, len(data)):
    num_list.append(data[i].strip().replace(" ", ","))

num_list2 = []

z = 1
for a in range(0, len(num_list)):
    num_list2.append([])
    new_str = num_list[a]
    k = 0

    for b in range(0, len(new_str)-z):

        num_list2[a].append(int(new_str[k]+new_str[k+1]))
        k = k+3
    z = z+2


for c in range(0, len(num_list2)-1):
    q = 0
    num_list2.append([])

    for d in range(0, len(num_list2[-3])):

        if num_list2[-2][q] >= num_list2[-2][q+1]:
            number = num_list2[-3][d]+num_list2[-2][q]
        else:
            number = num_list2[-3][d] + num_list2[-2][q+1]
        num_list2[-1].append(number)
        q = q+1
    del num_list2[-2]
    del num_list2[-2]


print("The mamimum total from top to bottom of the given triangle is {}".format(
    num_list2[0][0]))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))