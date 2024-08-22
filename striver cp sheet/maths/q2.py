t=int(input())
while t:
    a,b=map(int,input().split())
    if a*2<=b:
        print(a,a*2)
    else:
        print(-1,-1)
    t-=1