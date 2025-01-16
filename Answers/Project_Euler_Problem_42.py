import time
from math import sqrt


start_time = time.time()

data = open("Project Euler Problem 42 Resorces.txt", "r").read()
data = data.strip().split(",")
data = [x[1:-1] for x in data]

word_value_list = []

for i in range(0, len(data)):
    word = data[i]
    letter_list = list(word)
    word_value = 0
    for n in range(0, len(letter_list)):
        word_value += ord(letter_list[n])-64
    word_value_list.append(word_value)

triangle_word_value_list = []

for a in word_value_list:
    f = (sqrt(1+8*a)-1)/2
    if f == int(f):
        # print(a)
        triangle_word_value_list.append(f)

print("There are {} Triangle word in the given word list".format(
    len(triangle_word_value_list)))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
