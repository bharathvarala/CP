t=int(input())
while t:
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    if k==1 and a!=sorted(a):
        print("NO")
    else:
        print("YES")