import numpy as np

arr = np.array([1,3,4,7,3,1])

largest = arr[0]

for i in arr[1:]:
    if i > largest:
        largest = i
        
print(largest)

# print(np.max(arr))