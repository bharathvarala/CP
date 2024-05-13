from math import sqrt
#euler totient is count of numbers from (1,n) that are co-prime with n 
# phi(n) = n*((p1-1)/p1)....*((pk-1)/pk)
def prime(n):
    if n==1:
        return False
    if n==2 or n==3:
        return True
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False 
    return True


n=8
ans = n
if prime(n):
    print(n-1)
else:
    for i in range(2,int(sqrt(n))+2):
        if n%i==0:
            ans*=(i-1)
            ans//=i
            while n%i==0:
                n//=i 
            # print(n,ans)
    print(ans)