# cook your dish here
def f(a,x):
    b=x 
    for i in range(len(a)-1):
        b-=(a[i+1]-a[i])
        #print(b)
        if b<0:
            return False 
        if i!=len(a)-2:
            b=x 
    #print(x,b,a)
    for i in range(len(a)-1,0,-1):
        b-=(a[i]-a[i-1])
        if b<0:
            return False 
        if i!=1:
            b=x 
    return True 
t=int(input())
while t:
    n,x=map(int,input().split()) 
    a=list(map(int,input().split()))
    a=[0]+a
    a.append(x)
 
    for i in range(1,100001):
        if f(a,i):
            print(i)
            break 
    t-=1