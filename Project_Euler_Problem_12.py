from math import sqrt
import time

startime=time.time()

n=2
tri_num=3
divisor_list=[]


while len(divisor_list) <= 500:
    decimal_tri_num=sqrt(tri_num)
    for i in range(1,int(decimal_tri_num//1)):
        if tri_num % i == 0:
            divisor_list.append(i)
            divisor_list.append(tri_num/i)
    if len(divisor_list)<=500:
        divisor_list=[]
    else:
        print("The First Triangle Number to have over 500 Divisors is {}".format(tri_num))
    n += 1
    tri_num=n*(n+1)/2
    
endtime=time.time()

finishtime=endtime-startime
print("Code Took {} Seconds to Finish".format(finishtime))

# n=12375

# triangular_number = n*(n+1)/2
# print(triangular_number)
# from math import sqrt
# answer = 76576500

# sqrt_num = sqrt(answer)
# factor_list=[]

# for i in range(1, int(sqrt_num//1)):
#     if answer % i == 0:
#         factor_list.append(i)
#         factor_list.append(answer/i)

# print(len(factor_list))
