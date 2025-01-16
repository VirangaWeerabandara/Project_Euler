import time

start_time = time.time()

names = open("Project Euler Problem 22 Resorces.txt", "r").read()
names = names.strip().split(",")
print(names)
names = [x[1:-1] for x in names]
names.sort()

# print(names)

score_list = []

for i in range(0, len(names)):
    name = names[i]
    name_list = list(name)
    name_num_list = []
    for n in range(0, len(name_list)):
        name_num_list.append(ord(name_list[n])-64)
    score = (i+1)*sum(name_num_list)
    score_list.append(score)

print("Total of all the Name Scores in the given file is: {}".format(sum(score_list)))


finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
