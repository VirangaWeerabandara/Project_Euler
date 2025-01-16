from math import sqrt
x=1
n=1
t=1

status = False

while status==False:
    l=[]
    for i in range(1,int(sqrt(t))+1):    
        if t%i==0:
            l.append(i)
            
    if len(l)>250:
        status=True
        break   
    n+=1
    t=n*(n+1)/2

print(t)