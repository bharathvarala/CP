t=int(input())
while t:
    a,b,c=map(int,input().split())
    if a==b:
        if c&1:
            print("First")
        else:
            print("Second")
    else:
        if a>b:
            print("First")
        else:
            print("Second")
    t-=1