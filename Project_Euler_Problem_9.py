import time

start_time=time.time()

for c in range(5, 998):
    for b in range(4, 994):
        a = 1000 - (b + c)
        i=a*a+b*b
        k=c**c
        if a+b+c==1000 and a*a+b*b==c*c and a>0:
            answer=a*b*c
            print("a={}, b={}, c={}".format(a,b,c))
            print("abc = {}".format(answer))
            break
        
finish_time=time.time()

differnce=finish_time-start_time

print("Code took {} seconds to finish".format(differnce))
