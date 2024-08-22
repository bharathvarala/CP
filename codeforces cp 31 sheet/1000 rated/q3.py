t=int(input())
while t:
    n,p=map(int,input().split())
    a=list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = [[b[i],a[i]]for i in range(len(a))]
    c.append([p,n-1])
    n-=1
    c.sort(key = lambda x:(x[0],-x[1]))
    # print(c,n)
    ans=p
    for i in c:
        if n>0:
            if n<i[1]:
                ans+=(n*i[0])
                break 
            else:
                ans+=(i[1]*i[0])
                n-=i[1]
    print(ans)
    t-=1