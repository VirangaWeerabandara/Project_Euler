import time

start_time = time.time()

data=open("Project Euler Problem 81 Resorces - copy.txt","r").readlines()

matrix=[]
print(data)
for i in data:
    data_list=[int(x) for x in i.split(",")]
    matrix.append(data_list)

print(matrix)
matrix_len=len(matrix)

# for i in range(matrix_len-1,0,-1):
#     number1=matrix[i][i]+matrix[i][i-1]+matrix[i-1][i-1]
#     number2=matrix[i][i]+matrix[i-1][i]+matrix[i-1][i-1]
#     del matrix[i-1][i-1]
#     if number1<number2:
#         matrix[i-1].insert(i-1,number1)
#     elif number1>number2:
#         matrix[i-1].insert(i-1,number2)

# print(matrix[0][0])
# print(matrix)

# finish_time = time.time()

# duration = finish_time-start_time

# print("Programme took {} seconds to finish".format(duration))
