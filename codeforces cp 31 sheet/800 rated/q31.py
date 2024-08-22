from collections import Counter
from math import gcd
t=int(input())
while t:
    n,a,b  = map(int,input().split())
    if n==a and b==a:
        print("Yes")
    elif a+b<n-1:
        print("Yes")
 
    else:
        print("No")
    t-=1