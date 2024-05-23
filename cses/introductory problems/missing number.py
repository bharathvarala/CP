n=int(input())
a=list(map(int,input().split()))
s1 = sum(a)
s = (n*(n+1))//2
print(s-s1)