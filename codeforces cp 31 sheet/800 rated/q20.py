from collections import Counter
t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    ans=[]
    for i in a:
        ans.append(n-i+1)
    print(*ans)
    t-=1