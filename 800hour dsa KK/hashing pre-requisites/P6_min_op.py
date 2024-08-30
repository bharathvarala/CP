# min ops to make all elements equal 
# just print len(arr)-maxfreq

a=list(map(int,input().split()))
d={}
for i in a:
    if i not in d:
        d[i]=1 
    else:
        d[i]+=1
# print(d.values)
print(len(a)-max(list(d.values())))
