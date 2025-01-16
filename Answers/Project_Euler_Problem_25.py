import time

start_time = time.time()


def digits(x):
    digit_list = []
    while x >= 1:
        p = x % 10
        x = x//10
        digit_list.append(p)
    return len(digit_list)


fibinacci_sequence = [1, 1, 2]


while digits(fibinacci_sequence[-1]) < 1000:
    number = fibinacci_sequence[-1] + fibinacci_sequence[-2]
    fibinacci_sequence.append(number)

print(fibinacci_sequence.index(fibinacci_sequence[-1])+1)
print("Index of the first term in the fibinacci sequence to contain 1000 digits is {}".format(
    fibinacci_sequence.index(fibinacci_sequence[-1])+1))
# print(fibinacci_sequence)


finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
