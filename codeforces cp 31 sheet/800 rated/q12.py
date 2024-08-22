t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    ans=[a[0]]
    for i in range(1,len(a)):
        if ans[-1]<=a[i]:
            ans.append(a[i])
        else:
            ans.append(a[i])
            ans.append(a[i])
    print(len(ans))
    print(*ans)
    t-=1