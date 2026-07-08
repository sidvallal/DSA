arr = [0,1,2,3,5]

# for i in range(len(arr)):
#     if i not in arr:
#         print(i)
#         break

s = set(arr)
for i in range(len(arr)+1):
    if i not in s:
        print(i)
        break
