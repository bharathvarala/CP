t=int(input())
while t:
    n,k,x = map(int,input().split())
    if k==1 and x==1:
        print("NO")
    
    elif (k==2 and x==1 and n&1):
        print("NO")
    elif (x==1 and k==1 and n&1==0):
        print("YES")
        print(n//2)
        print(*[2 for i in range(n//2)])
    elif (x==2 and k==2 and n&1):
        print("YES")
        print(n)
        print(*[1 for i in range(n)])
    else:
        if x!=1:
            print("YES")
            print(n)
            print(*[1 for i in range(n)])
        else:
            print("YES")
            a=[]
            while n>2:
                a.append(2)
                n-=2
            if n==2:
                a.append(2)
                print(len(a))
                print(*a)
            else:
                a.pop()
                a.append(3)
                print(len(a))
                print(*a)
    t-=1