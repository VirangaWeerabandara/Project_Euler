import time

start_time = time.time()

numbers = []
making_number = 100

for x in range(1, 100):
    numbers.append(x)


def chart(x, y):
    answer_list = [[0]]
    for a in y:
        answer_list.append([a])

    for b in range(0, x+1):
        answer_list[0].append(b)

    for c in range(1, x+2):
        if answer_list[0][c] % y[0] == 0:
            answer_list[1].append(1)
        else:
            answer_list[1].append(0)
    return answer_list


answer_chart = chart(making_number+1, numbers)


for i in range(2, len(numbers)+1):
    for j in range(0, making_number+1):
        if j < numbers[i-1]:
            answer_chart[i].append(answer_chart[i-1][j+1])
        else:
            answer_chart[i].append(
                answer_chart[i-1][j+1]+answer_chart[i][j+1-numbers[i-1]])

print("There are {} ways one hundred can be written as a sum of at least two positive integers ".format(
    answer_chart[-1][-1]))

end_time=time.time()

difference= end_time-start_time

print("Code took {} seconds to execute".format(difference))