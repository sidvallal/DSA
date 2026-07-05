import numpy as np

arr = np.array([5,4,3,2,1])

l = 0
r = len(arr)-1

while l <= r:
    temp = arr[l]
    arr[l] = arr[r]
    arr[r] = temp
    
    l+=1
    r-=1
    
print(arr)

# print(arr[::-1])
