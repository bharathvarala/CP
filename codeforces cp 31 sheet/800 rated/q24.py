from collections import Counter
t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    ans=-1
    c=0
    for i in range(257):
        x=[k^i for k in a]
        y=0
        for j in x:
            y^=j
        if y==0:
            c=1
            ans=i
            break
    if not c:
        print(-1)
    else:
        print(ans)
        
    t-=1