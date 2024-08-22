from collections import Counter
t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    ans=0
    for i in range(len(a)):
        if a[i]==0:
            c+=1
        else:
            ans=max(c,ans)
            c=0
    ans=max(ans,c)
    print(ans)
    t-=1