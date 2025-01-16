import time
from math import factorial

start_time = time.time()

grid_length = 20

n = grid_length*2
r = grid_length

answer = factorial(n)/(factorial(r)*factorial(n-r))

print("There are {} routs through a 20x20 grid".format(int(answer)))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
