t=int(input())
while t:
    a=list(map(int,input().split()))
    m=max(a)
    if a.count(m)<2:
        print("NO")
    else:
        print("YES")
        print(min(a),min(a),m)
    t-=1