
def power(a,n):
    if n==0:
        return 1
    if n==1:
        return a
    if n&1==0:
        return power(a,n//2)*power(a,n//2)
    return a*power(a,n//2)*power(a,n//2)
print(power(2,3))