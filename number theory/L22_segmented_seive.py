# problem - https://www.geeksforgeeks.org/problems/find-prime-numbers-in-a-range4718/1

from math import sqrt
l=1 
r = 150 
p=[True]*(int(sqrt(r))+1)
p[0],p[1]=False,False 
for i in range(2,int(sqrt(len(p)))+1):
    if p[i]:
        j=2*i 
        while j<len(p):
            p[j]=False 
            j+=i 
d={}
for i in range(len(p)):
    if p[i]:
        d[i]=1 
plr = [True]*(r-l+1)
# print(d)
for i in d:
    for j in range(l,r+1):
        # print(j,i)
        f=0
        if j%i==0:
            # print(j,i)
            f=1
            k=j 
            while (k-l)<len(plr):
                # print(k-l)
                plr[k-l]=False 
                k+=i 
        if f:
            break 
print(plr)
print(plr[149-l])
    