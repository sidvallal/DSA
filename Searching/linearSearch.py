def linearSearch(arr,key):

    for i in range(len(arr)):
        if arr[i] == key:

            return "Found at Index : ", i

    return "Not Found"


arr = [1,2,3,4,5,6,7]

print(linearSearch(arr,10))