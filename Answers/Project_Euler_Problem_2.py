import time

start_time=time.time()

no_1 = 1
no_2 = 2
finallist = [2]

while no_2 < 100:
    no_1=no_1+no_2
    no_2=no_2+no_1
    if no_1 % 2 == 0:
        finallist.append(no_1)

    if no_2%2==0 :
        finallist.append(no_2)
   
    

print(sum(finallist))

finish_time=time.time()

differnce=finish_time-start_time

print("Code took {} seconds to finish".format(differnce))
