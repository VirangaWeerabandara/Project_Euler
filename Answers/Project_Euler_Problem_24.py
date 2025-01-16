import time
from itertools import permutations

start_time = time.time()

num_permutaions = list(permutations(range(0,10)))

print("Millionth lexicographic permutation of the digits 0,1,2,3,4,5,6,7,8,9 is {}".format(num_permutaions[999999]))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))