from collections import Counter
t=int(input())
while t:
    a,b,c,d = map(int,input().split())
    if b==d:
        if a<c:
            print(-1)
        else:
            print(abs(a-c))
    else:
        if d>b:
            if (d-b)+a<c:
                print(-1)
            else:
                print(2*(d-b)+a-c)
        else:
            print(-1)
    t-=1