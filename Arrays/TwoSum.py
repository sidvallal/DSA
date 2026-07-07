import numpy as np

arr = np.array([2,4,2,1,3,5,1])

target = 7

# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] + arr[j] == target:
#             print('yes')
#             print(arr[i], arr[j])
#             break

seen = {}

for i,num in enumerate(arr):
    comp = target - num
    
    if comp in seen :
        print("Indices : ",seen[comp],i)
        break
    seen[num] = i


            

        