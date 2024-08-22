n=int(input())
a=list(map(int,input().split()))
p=10**9
n=-10**9
c=0
for i in a:
    if i>0:
        p=min(p,i)
    elif i<0:
        n=max(n,i)
    else:
        c=1
        break
if c:
    print(0)
else:
    print(min(p,n*-1))