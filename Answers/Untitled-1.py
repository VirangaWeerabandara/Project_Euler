# from math import sqrt

# def is_prime(number):
#     list1 = []
#     if number<=0:
#         return False

#     if number==1:
#         return False

#     for i in range(2, int(sqrt(number))+1):
#         if number % i == 0:
#             while number % i == 0:
#                 number = number/i
#                 list1.append([i,number/i])
                
#     return list1
    
# print(sqrt(4999999999995))
status=False
n=2236067
parameter_1=9999999999990


while status==False:
    number=n*(n+1)*2
    if number > parameter_1:
        status=True
    n+=1
    
print(n+1)