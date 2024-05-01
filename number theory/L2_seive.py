#for 10**6 numbers
from math import sqrt
arr = [True]*(10**6 + 2)
arr[0],arr[1]=False,False

for i in range(2,int(sqrt(len(arr)))+1):
    if arr[i]:
        j = i*2 
        while j<len(arr):
            arr[j]=False
            j+=i
print(arr[1001])
