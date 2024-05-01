from math import sqrt

n=123
def prime(n):
    if n==1:
        return False
    if n==2 or n==3:
        return True
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False 
    return True

print(prime(n))