t=int(input())
while t:
    n=int(input())
    a=[]
    for i in range(n):
        m=int(input())
        a.append(list(map(int,input().split())))
    for i in a:
        i.sort()
    a.sort()
    s=[i[1] for i in a]
    s.sort()
    # print(s)
    ans=sum(s)
    ans-=s[0]
    # print(ans)
    ans+=a[0][0]
    print(ans)
    t-=1

