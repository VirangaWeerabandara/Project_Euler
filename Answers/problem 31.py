import time

start_time=time.time()

coins=[1,2,5,10,20,50,100,200]
making_number=200

def chart(x,y):
    answer_list=[[0]]
    for a in y:
        answer_list.append([a])
    
    for b in range(0,x+1):
        answer_list[0].append(b)

    for c in range(1,x+2):
        if answer_list[0][c]%y[0]==0:
            # print(answer_list[0][c],c)
            answer_list[1].append(1)
        else:
            answer_list[1].append(0)
    # print(len(answer_list[0]),len(answer_list[1]))
    return answer_list    

# print(chart(200,coins))

answer_chart=chart(making_number+1,coins)


# print(answer_chart)

for i in range(2,len(coins)+1):
    for j in range(0,making_number+1):
        if j<coins[i-1]:
            # print(j,coins[i-1])
            answer_chart[i].append(answer_chart[i-1][j+1])
        else:
            # print(answer_chart[i][j-coins[i-1]],i,j,coins[i-1])
            answer_chart[i].append(answer_chart[i-1][j+1]+answer_chart[i][j+1-coins[i-1]])

print(answer_chart[-1][-1])

