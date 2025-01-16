import time

start_time=time.time()

squares_sum=[]
sum_list=[]

for i in range(1,101):
    square_number=i*i
    squares_sum.append(square_number)

for k in range(1,101):
    sum_list.append(k)

difference=sum(sum_list)**2-sum(squares_sum)

print(difference)

finish_time=time.time()

differnce=finish_time-start_time

print("Code took {} seconds to finish".format(differnce))
