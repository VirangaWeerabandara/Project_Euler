import time


start_time=time.time()

content = open("Project Euler Problem 8 Resorces.txt","r").read()

num_list = list(content)

##   another way for converting in to a list

# for i in range(0, len(content)):
#     num_list.append(content[i])


def multiplication(a):
    number=1
    for i in range(a,a+13):
       
        number=number*int(num_list[i])
    return(number)

max_product=0
a=0

for n in range(0, 987):
   
    cal_product = multiplication(a)

    if cal_product > max_product:
        max_product = cal_product
        a = a+1
    else:
        a = a+1

print("Product of the Thirteen adjacent digits in the 1000-digit number is: {} ".format(max_product))

finish_time=time.time()

duration = finish_time - start_time

print("This Programme took {} seconds to Finish".format(duration))