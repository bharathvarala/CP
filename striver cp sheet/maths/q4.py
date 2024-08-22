t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    d={}
    for i in a:
        if i&1:
            if "o" in d:
                d["o"]+=1 
            else:
                d["o"]=1 
        else:
            if "e" in d:
                d["e"]+=1 
            else:
                d["e"]=1
    if len(d)==2 or (len(d)==1 and "o" in d and d["o"]&1):
        print("YES")
    else:
        print("NO")
    t-=1  
