
def power(a,n):
    if n==0:
        return 1
    if n==1:
        return a
    if n&1==0:
        return power(a,n//2)*power(a,n//2)
    return a*power(a,n//2)*power(a,n//2)
print(power(5,4))

#iterative approach 

ans=1
a=5
n=4
while n:
    if n&1:
        ans*=a
        n-=1
    else:
        a*=a
        n//=2 
print(ans) 
    