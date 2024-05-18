#check for all possibilities using a,b,c,d 
#Optimal : Only b,c,c is enough


t=int(input())
def f(x,y,z):
    return (x+y>z and x+z>y and y+z>x)
while t:
    a,b,c,d = map(int,input().split())
    if f(a,b,c):
        print(a,b,c)
    elif f(a,b,d):
        print(a,b,d)
    elif f(a,c,d):
        print(a,c,d)
    elif f(b,c,d):
        print(b,c,d)
    elif f(b,b,c):
        print(b,b,c)
    elif f(b,b,d):
        print(b,b,d)
    elif f(a,c,c):
        print(a,c,c)
    elif f(b,c,c):
        print(b,c,c)
    t-=1