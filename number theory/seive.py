#for 10**6 numbers

arr = [True]*(10**6 + 2)
arr[0],arr[1]=False,False

for i in range(2,len(arr)):
    if arr[i]:
        j = i*2 
        while j<len(arr):
            arr[j]=False
            j+=i
print(arr[19])