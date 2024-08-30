from collections import Counter
n=list(map(int,input().split()))
m=list(map(int,input().split()))
d1=Counter(n)
d2=Counter(m)
f=0
for i in d2:
    if i not in d1 or (i in d1 and d1[i]<d2[i]):
        f=1 
        print("No")
        break 
if not f:
    print("Yes")
