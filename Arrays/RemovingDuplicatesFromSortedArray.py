import numpy as np

arr = np.array([1,2,2,3,4,5,5])
print(arr)

j = 0

for i in range(1,len(arr)):
    if arr[i] != arr[j]:
        j+=1
        arr[j] = arr[i]

print(arr[:j+1])
    
    
# res = np.array([], dtype=int)



# prev = 0 
# for i in arr:
#     if i>prev:
#         res = np.append(res,i)
#         prev = i
    
# print(res)