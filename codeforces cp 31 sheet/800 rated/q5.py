t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    
    for j in range(n):
        for i in range(1,n-1):
            if a[i-1]<a[i] and a[i]>a[i+1]:
                a[i+1],a[i]=a[i],a[i+1]
    if a==sorted(a):
        print("YES")
    else:
        print("NO")
    t-=1