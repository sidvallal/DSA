import numpy as np

arr = np.array([1,2,2,3,3,4,4])

res = 0 

for i in arr:
    res ^=i
    
print(res)