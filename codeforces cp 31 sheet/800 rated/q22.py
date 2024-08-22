from collections import Counter
t=int(input())
while t:
    n,k=map(int,input().split())
    if k==1:
        print("YES")
    elif n%2==0 or n%k==0:
        print("YES")
    elif (n-k)&1:
        print("NO")
    else:
        print("YES")
    t-=1