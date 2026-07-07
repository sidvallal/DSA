import numpy as np

# hash = {
#     'name' : 'sid',
#     'age' : 20,
# }


# for key in hash:
#     print(key)
    
# print()
    
# for value in hash.values():
#     print(value)
    
# print()
    
# for key,value in hash.items():
#     print(key, value)
    
# arr = np.array([1,1,2,1,2,2])

# freq = {}

# for i in arr:
#     freq[i] = freq.get(i,0) + 1

# print(freq)

arr = [2, 7, 11, 15]
target = 26

seen = {}

for i, num in enumerate(arr):
    comp = target - num
    
    if comp in seen:
        print(seen[comp],i)
        break
    
    seen[num] = i

