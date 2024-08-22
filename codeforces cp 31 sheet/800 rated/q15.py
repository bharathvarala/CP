t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    x=[0,0]
    for i in a:
        if i&1:
            x[0]+=1
        else:
            x[1]+=1
    if x[0]:
        if x[0]&1:
            print("NO")
        else:
            print("YES")
    else:
        print("YES")
    t-=1