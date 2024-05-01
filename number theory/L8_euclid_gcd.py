def gcd(a,b):
    if b==0:
        return a 
    return gcd(b,a%b)

#iterative

a = 140 
b = 12
gcd = -1
while b:
    if b==0:
        gcd = a
    c = a
    a = b
    b = c%b 
    # print(a,b)
    if b==0:
        gcd = a
print(gcd)