import time
from collections import Counter
from statistics import mode

start_time = time.time()

cypher = open("Project Euler Problem 59 Resorces.txt", "r").read()
cypher = cypher.strip().split(",")

cypher_edit_1 = []
cypher_edit_2 = []
cypher_edit_3 = []

for a in range(0, len(cypher)-2, 3):
    cypher_edit_1.append(int(cypher[a]))
    cypher_edit_2.append(int(cypher[a+1]))
    cypher_edit_3.append(int(cypher[a+2]))

key1 = ord(" ") ^ mode(cypher_edit_1)
key2 = ord(" ") ^ mode(cypher_edit_2)
key3 = ord(" ") ^ mode(cypher_edit_3)

decrypted_cypher = []

for i in range(0, len(cypher)-2, 3):
    new1 = int(cypher[i]) ^ key1
    new2 = int(cypher[i+1]) ^ key2
    new3 = int(cypher[i+2]) ^ key3
    decrypted_cypher.append(new1)
    decrypted_cypher.append(new2)
    decrypted_cypher.append(new3)

# print(decrypted_cypher)
# new_cypher=""
# for n in decrypted_cypher:
#     new_cypher+=str(n)

print("Sum of the ASCII values in the original text is {}".format(
    sum(decrypted_cypher)))


finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
