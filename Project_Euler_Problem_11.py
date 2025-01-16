import time

start_time = time.time()

data=open("Project Euler Problem 11 Resorces.txt","r").readlines()

num_list = []


for i in range(0, len(data)):
    num_list.append(data[i].strip().replace(" ", ","))

num_list2 = []
grid_length=20

for a in range(0, len(num_list)):
    num_list2.append([])
    new_str = num_list[a]
    k = 0

    for b in range(0,grid_length):

        num_list2[a].append(int(new_str[k]+new_str[k+1]))
        k = k+3
    
#print(num_list2)

product_list=[]

for n in range(0,20):
    for i in range(0,grid_length-3):
        number1=num_list2[n][i]*num_list2[n][i+1]*num_list2[n][i+2]*num_list2[n][i+3]
        # a1=num_list2[n][i]
        # a2=num_list2[n][i+1]
        # a3=num_list2[n][i+2]
        # a4=num_list2[n][i+3]
        product_list.append(number1)
        
for x in range(0,grid_length-3):
    for y in range(0,20):
        number2=num_list2[x][y]*num_list2[x+1][y]*num_list2[x+2][y]*num_list2[x+3][y]
        # a1=num_list2[x][y]
        # a2=num_list2[x+1][y]
        # a3=num_list2[x+2][y]
        # a4=num_list2[x+3][y]
        product_list.append(number2)
    
for p in range(0,grid_length-3):
    for q in range(0,grid_length-3):
        number3=num_list2[p][q]*num_list2[p+1][q+1]*num_list2[p+2][q+2]*num_list2[p+3][q+3]
        # a1=num_list2[p][q]
        # a2=num_list2[p+1][q+1]
        # a3=num_list2[p+2][q+2]
        # a4=num_list2[p+3][q+3]
        product_list.append(number3)

for v in range(0,grid_length-3):
    for u in range(grid_length-1,0,-1):
        number4=num_list2[v][u]*num_list2[v+1][u-1]*num_list2[v+2][u-2]*num_list2[v+3][u-3]
        # a1=num_list2[v][u]
        # a2=num_list2[v+1][u-1]
        # a3=num_list2[v+2][u-2]
        # a4=num_list2[v+3][u-3]
        product_list.append(number4)

print("The greates product of four adjacent numbers in the same direction(up,down,left,right,diagonally) in the given 20x20 grid is {}".format(max(product_list)))

finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
