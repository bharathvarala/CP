from collections import Counter
t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    d=Counter(a)
    # print(d)
    if len(d)==1:
        print("YES")
    elif len(d)==2:
        s=[d[i] for i in d]
        # s.sort()
        if s[0]==s[1] or s[0]==s[1]+1 or s[1]==s[0]+1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    t-=1