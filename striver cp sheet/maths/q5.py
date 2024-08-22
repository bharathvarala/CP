t=int(input())
while t:
    n,x = map(int,input().split())
    a = 2
    ans =1 
    while a<n:
        ans+=1 
        a+=x 
    print(ans)
    t-=1