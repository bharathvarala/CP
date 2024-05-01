
# m = [[1,2,3],[4,5,6],[7,8,9]]
mod = 10**9+7
def mul(m,a):
    ans = [[0 for i in range(len(m[0]))]for j in range(len(m))]
    # print(ans)
    for i in range(len(m)):
        for j in range(len(m)):
            for k in range(len(m)):
                ans[i][j]=(ans[i][j]%mod + m[i][k]%mod * a[k][j]%mod)%mod
    return ans


t = int(input())
while t:
    a,n = map(int,input().split())
    m=[]
    for i in range(a):
        m.append(list(map(int,input().split())))
    
    idn = [[0 for i in range(len(m[0]))]for j in range(len(m))]
    for i in range(len(idn)):
        for j in range(len(idn)):
            if i==j:
                idn[i][j] = 1
    while n:
        if n&1:
            idn = mul(m,idn)
            n-=1
        else:
            m = mul(m,m)
            n//=2
    for i in idn:
        print(*i)
    t-=1