from collections import Counter
t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    d=Counter(a)
    if 1 not in d:
        if d[-1]&1:
            x=d[-1]//2 + 1 
            if (n-x)&1==0:
                print(x)
            else:
                print(x+1)
        else:
            x=d[-1]//2
            if (n-x)&1:
                print(x+1)
            else:
                print(x)
    elif d[-1]==0:
        print(0)
    else:
        x=d[1]
        y=d[-1]
        ans=0
        while y>x or y&1:
            # print(y,x)
            ans+=1
            y-=1
            x+=1
        print(ans)
    
    t-=1