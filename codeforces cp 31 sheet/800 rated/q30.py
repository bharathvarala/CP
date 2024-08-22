t=int(input())
while t!=0:
    n=int(input())
    x=list(str(n))
    s=0
    s+=(len(x)-1)*9 + int(x[0])
    print(s)
    t-=1