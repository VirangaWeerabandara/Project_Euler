import time
from itertools import permutations

start_time = time.time()

number_list = []
string_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
permutation_list = list(permutations(string_list))


for i in range(0, len(permutation_list)):
    permutation_list[i] = int("".join(map(str, permutation_list[i])))
    if len(str(permutation_list[i])) == 10:
        str_num = str(permutation_list[i])
        if int(str_num[3]) % 2 == 0:
            if int(str_num[2:5]) % 3 == 0:
                if int(str_num[5]) % 5 == 0:
                    if int(str_num[4:7]) % 7 == 0:
                        if int(str_num[5:8]) % 11 == 0:
                            if int(str_num[6:9]) % 13 == 0:
                                if int(str_num[7:10]) % 17 == 0:
                                    number_list.append(permutation_list[i])
                                else:
                                    continue
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            continue

print("sum of all the pandigital numbers with the given property if {}".format(
    sum(number_list)))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
