import time

start_time = time.time()

status = False
n = 345

while status == False:
    number = n+1
    n_list = list(str(n**3))
    n_list.sort()
    answer_list = []
    while len(str(n**3)) == len(str(number**3)):
        number_list = list(str(number**3))
        number_list.sort()
        if number_list == n_list:
            answer_list.append(number)
        if len(answer_list) == 4:
            print(
                "{} is the cube which exactly five permutations of its digits are cube".format(n**3))
            status = True
            break
        number += 1
    n += 1


end_time = time.time()

difference = end_time-start_time

print("Code took {} seconds to execute".format(difference))
