# cook your dish here
t=int(input())
while t:
    n=int(input())
    s=input()
    c=0 
    x=0
    a=[]
    ans=0
    for i in s:
        if i==".":
            c+=1 
        else:
            if c:
                a.append(c)
            c=0 
    if c:
        a.append(c)
    f=0
    if s.count(".")==0:
        print(0)
    else:
        #print(a)
        for i in a:
            if i==1:
                ans+=1
            elif i==2:
                ans+=2
            else:
                f=1
                break 
        if not f:
            print(ans)
        else:
            print(2)
    t-=1