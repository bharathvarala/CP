t=int(input())
while t!=0:
    n=int(input())
    a=input()
    i=0
    j=len(a)-1
    x=len(a)
    while i<j:
        if (a[i]=="0" and a[j]=="1") or (a[i]=="1" and a[j]=="0"):
            x-=2
            j-=1
            i+=1
        else:
            break
    print(x)
    t-=1