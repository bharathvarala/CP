from collections import Counter
from math import gcd
t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    p=1
    for i in a:
        p*=i
    ans=-1
    p//=a[0]
    q=a[0]
    for i in range(1,len(a)):
        if p==q:
            ans=i
            break
        p//=a[i]
        q*=a[i]
    print(ans)
        
    t-=1