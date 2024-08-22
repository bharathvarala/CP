t=int(input())
while t:
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    if k not in a:
        print("NO")
    else:
        print("YES")
    t-=1