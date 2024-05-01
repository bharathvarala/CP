# 100 => 2**2 * 5**2 
from math import sqrt 
# Brute force 
def prime(n):
    if n==1:
        return False
    if n==2 or n==3:
        return True
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False 
    return True
n = 24
x = n
for i in range(2,int(sqrt(n))+1):
    if n%i==0:
        c=0
        while n%i==0:
            c+=1
            n//=i
        print(str(i)+"^"+str(c))
if n>1:
    print(str(n)+"^"+"1")