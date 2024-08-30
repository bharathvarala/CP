# min and max frequency in the array 
from collections import Counter
a=list(map(int,input().split()))
# k=int(input())  
d=Counter(a)
m,mv,mi,miv = -10**9,0,10**9,0
for i in d:

    if d[i]>m:
        m = d[i]
        mv = i 
    if d[i]<mi:
        mi = d[i]
        miv = i 
print(mv,m)
print(miv,mi)
