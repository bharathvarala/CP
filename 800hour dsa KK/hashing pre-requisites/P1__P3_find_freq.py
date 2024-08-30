from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
d=defaultdict()
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1  
q=list(map(int,input().split()))
for i in q:
    if i in d:
        print(i,d[i])
    else:
        print(i,0)