from collections import *
t=int(input())
while t!=0:
    n=int(input())
    a=list(map(int,input().split()))
    x=Counter(a)
    z=0
    for i in x:
        if x[i]==len(a):
            z=1
            print("NO")
            break
    if z==0:
        print("YES")
        c=[]
        a.sort()
        while len(a)!=0:
            c.append(a.pop())
            if len(a)==0:
                break
            c.append(a.pop(0))
        print(*c)
    t-=1
        