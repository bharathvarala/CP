t=int(input())
while t:
    n,m=map(int,input().split())
    x=input()
    s=input()
    c=6
    ans=0
    f=0
    while c:
        if s in x:
            f=1
            break
        else:
            ans+=1
            x+=x
        c-=1
    if f:
        print(ans)
    else:
        print(-1)
            
    t-=1