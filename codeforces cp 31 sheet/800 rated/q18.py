t=int(input())
while t:
    n,k = map(int,input().split())
    if n%k!=0:
        print(1)
        print(n)
    else:
        a=n
        while n%k==0:
            n-=1
        print(2)
        print(a-n,n)
    
    t-=1