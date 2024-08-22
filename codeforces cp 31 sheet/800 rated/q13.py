t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    if len(set(a))==1:
        print(-1)
    else:
        m=max(a)
        i=-1
        for j in range(len(a)):
            if a[j]==m:
                i=j
                break
        b=a[:j]
        c=a[j:]
        print(len(b),len(c))
        print(*b)
        print(*c)
    t-=1