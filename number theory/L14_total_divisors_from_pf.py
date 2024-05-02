mod = 10**9 + 7
t=int(input())
while t:
    n=int(input())
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    
    ans = 1
    for i in a:
        ans = (ans%mod * (i[1]%mod+1%mod))%mod
    print(ans)
    t-=1