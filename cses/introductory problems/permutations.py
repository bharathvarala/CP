n=int(input())
if n in (2,3):
    print("NO SOLUTION")
else:
    ans=[]
    for i in range(2,n+1,2):
        ans.append(i)
    for i in range(1,n+1,2):
        ans.append(i)
    print(*ans)