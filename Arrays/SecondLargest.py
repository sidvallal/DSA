import numpy as np

arr = np.array([1,2,3,4,5,7,1,6])

largest = arr[0]
second = float('-inf')

for i in arr[1:]:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print(second)