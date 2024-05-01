
p = [-1]*52

for i in range(2,len(p)):
    if p[i]==-1:
        p[i]=i
        j=i*2
        while j<len(p):
            if p[j] == -1:
                p[j]=i
            j+=i

n = 27
a=[]
while n>1:
    a.append(p[n])
    n//=p[n]
print(a)