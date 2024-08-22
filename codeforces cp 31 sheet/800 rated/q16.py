t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    if a!=sorted(a):
        print(0)
    else:
        ans=10**9
        for i in range(len(a)-1):
            ans=min((a[i+1]-a[i])//2 + 1,ans)
        print(ans)
    t-=1