from math import sqrt
# calculate sum(gcd(i,n)) for 1<=i<=n

n = 12
p=[i for i in range(0,n+2)]
for i in range(2,len(p)):
    if p[i]==i:
        p[i]=i-1
        j=i*2 
        while j<len(p):
            p[j]*=(i-1)
            p[j]//=i 
            j+=i
print(p)
ans = 0
#for 12 --> 1*4 + 2*2 + 3*2 + 4*2 + 6*1 + 12*1 = 4+4+6+8+18 = 40
for i in range(1,int(sqrt(n))+1):
    if n%i==0:
        # print(i)
        d1 = i
        d2 = n//i 
        # print(d1,d2,p[n//d1],p[n//d2])
        ans+=d1*p[n//d1]
        print(ans)
        if d1!=d2:
            ans+=d2*p[n//d2]
print(ans)