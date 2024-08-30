a=list(map(int,input().split()))
k=int(input())
d={}
f=0
for i in range(len(a)):
    if a[i] in d:
        if i-d[a[i]]<=k:
            f=1
            print("Yes")
            break 
    d[a[i]]=i 
if not f:
    print("No")