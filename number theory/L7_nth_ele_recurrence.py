f = [0,1]
m = [[0,3],[1,2]]

idn = [[1,0],[0,1]]

def mul(m,a):
    ans = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ans[i][j] += m[i][k]*a[k][j]
    return ans 

n = 4
n-=1 
while n:
    if n&1:
        idn = mul(m,idn)
        n-=1
    else:
        m = mul(m,m)
        n//=2 
print(f[0]*idn[0][0] + f[1]*idn[1][0])