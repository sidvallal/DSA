import numpy as np

nums = np.array([4,5,0,1,9,0,5,0])
print(nums)

left = 0

for right in range(len(nums)):
    if nums[right] != 0:
        nums[left],nums[right] = nums[right],nums[left]
        left+=1
        
print(nums)