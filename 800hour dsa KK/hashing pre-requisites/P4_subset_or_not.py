n=list(map(int,input().split()))
m=list(map(int,input().split()))
s1,s2=set(),set()
for i in n:
    s1.add(i)
for i in m:
    s2.add(i)
f=0
for i in s2:
    if i not in s1:
        f=0
        print("No")
        break 
if not f:
    print("Yes")
