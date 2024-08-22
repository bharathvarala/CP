from collections import Counter
from math import gcd
t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    o=[]
    c=0
    for i in a:
        if i&1:
            c+=1
        else:
            if c:
                o.append(c)
                c=0
    if c:
        o.append(c)
    c=0
    for i in a:
        if i&1==0:
            c+=1
        else:
            if c:
                o.append(c)
                c=0
    if c:
        o.append(c)
    # print(o)
    ans=0
    for i in o:
        ans+=(i-1)
    print(ans)
    t-=1