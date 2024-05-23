n=int(input())
ans=[n]
while n>1:
    if n&1:
        ans.append(n*3+1)
        n*=3
        n+=1 
    else:
        ans.append(n//2)
        n//=2
print(*ans)
