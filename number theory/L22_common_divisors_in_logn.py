from math import sqrt
n,q=map(int,input().split())
dn={}
for i in range(2,int(sqrt(n))+1):
    if n%i==0:
        a=0
        while n%i==0:
            n//=i
            a+=1 
        dn[i]=a  
# print(dn)
def f(k,d):
    dk={}
    for i in d:
        a=0
        while k%i==0:
            # print(k,i)
            a+=1
            k//=i 
        dk[i]=a  
    # print(dk)
    ans=1 
    for i in d:
        m=min(d[i],dk[i])
        ans*=(m+1)
    return ans 
while q:
    k=int(input())
    print(f(k,dn))
    q-=1 