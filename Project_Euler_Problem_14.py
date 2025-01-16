import time

start_time=time.time()
def is_number_even(i):
    
    if  i%2==0:
        number_even=True
    else:
        number_even = False
    
    return(number_even)
n=1000000

len_list=[]
number_list=[]

while n>=13:
    i=n      
    current_list=[]
    while i > 1:   
        if is_number_even(i)==True:
            i=i/2
        else:
            i=3*i+1
        current_list.append(i)
    len_list.append(len(current_list))
    current_list=[]
    number_list.append(n)
    n=n-1
    

print("Starting Number under one Million which produce the largest chain is {} ".format(number_list[len_list.index(max(len_list))]))

end_time=time.time()

difference=end_time-start_time

print("programme took {} seconds calculate".format(difference))