# given array and l and r. Find gcd of array excluding elements from l to r for each query

#Solution :
'''
Solution : 1) Construct prefix and suffix array 
           2) consider gcd of 1 to l-1 from prefix array (g1)
           3) consider gcd of R+1 to n from prefix array (g2)
           4) gcd(g1,g2) is ans for query 
'''
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
n,k = map(int,input().split())
a = list(map(int,input().split()))
q = []
for i in range(k):
    q.append(list(map(int,input().split())))
pg = [a[0]]
for i in range(1,len(a)):
    # print(a[i],pg[-1],gcd(a[i],pg[-1]))
    pg.append(gcd(a[i],pg[-1]))
sg = [a[-1]]
for i in range(len(a)-2,-1,-1):
    sg.append(gcd(a[i],sg[-1]))
for i in q:
    l=i[0]
    r=i[1]
    if l==1 and r==n:
        print(0)
    elif l==1:
        print(sg[r])
    elif r==n:
        print(pg[l-2])
    else:
        print(gcd(sg[r],pg[l-2]))
