arr = [1,2,3,1,2,3,3,2,2,4]

freq = {}

for num in arr:
    freq[num] = freq.get(num,0) + 1
    
for key, value in freq.items():
    print(key," -> ",value)
