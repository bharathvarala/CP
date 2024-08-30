a=list(map(int,input().split()))
k=int(input())
d={}
f=0
for i in a:
    if i in d:
        d[i]+=1 
    else:
        d[i]=1 
for i in range(len(a)):
    x=k-a[i]
    if x in d:
        f=1 
        break 
if f:
    print("Yes")
else:
    print("No")

