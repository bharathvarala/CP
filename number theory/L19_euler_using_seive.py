from math import sqrt
p = [i for i in range(0,13)]
n = 12

for i in range(2,len(p)):
    if p[i]==i:
        p[i] = i-1
        j = i*2
        while j<len(p):
            p[j]//=i 
            p[j]*=(i-1)
            j+=i
print(p[9])
