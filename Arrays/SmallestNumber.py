arr = [5,4,3,27,1,3,3]

small = arr[0]

for i in arr[1:]:
    if i < small:
        small = i
        
print(small)

