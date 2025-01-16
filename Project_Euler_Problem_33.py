import time,numpy
from fractions import Fraction

start_time = time.time()


def digts(x, y):
    digit_list = []
    num = [x, y]
    for i in num:
        while i >= 1:
            ans = i % 10
            i = i//10
            digit_list.append(ans)
    #digit_list = list(dict.fromkeys(digit_list))
    digit_list1 = [a for a in digit_list if a != 0]
    return digit_list, digit_list1

numerator_list=[]
denominator_list=[]


# print(digts(12,6100))


for i in range(10, 100):
    for n in range(i+1, 100):
        if len(digts(i, n)[0]) == len(digts(i, n)[1]):
            new_list=digts(i,n)[0]
            # for a in range()
            if new_list[0]==new_list[2] :
                new_list.remove(new_list[0]) 
                new_list.remove(new_list[1])
                #print(new_list)
                if i/n==new_list[0]/new_list[1]:
                    #print(i,n)
                    numerator_list.append(i)
                    denominator_list.append(n)
                continue
            if new_list[0]==new_list[3] :
                new_list.remove(new_list[0]) 
                new_list.remove(new_list[2])
                #print(new_list)
                if i/n==new_list[0]/new_list[1]:
                    #print(i,n)
                    numerator_list.append(i)
                    denominator_list.append(n)
                continue
            if new_list[1]==new_list[2] :
                new_list.remove(new_list[1]) 
                new_list.remove(new_list[1])
                #print(new_list)
                if i/n==new_list[0]/new_list[1]:
                    #print(i,n)
                    numerator_list.append(i)
                    denominator_list.append(n)
                continue
            if new_list[1]==new_list[3] :
                new_list.remove(new_list[1]) 
                new_list.remove(new_list[2])   
                #print(new_list)
                if i/n==new_list[0]/new_list[1]:
                    #print(i,n)
                    numerator_list.append(i)
                    denominator_list.append(n)
                continue

ab=numpy.prod(numerator_list)
bc=numpy.prod(denominator_list)

print(Fraction(ab,bc))


finish_time = time.time()

duration = finish_time-start_time

print("Programme took {} seconds to finish".format(duration))
