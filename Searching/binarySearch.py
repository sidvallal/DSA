def BinarySearch(arr,key):

    low = 0
    high = len(arr)-1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == key:
            return "Element Found at Index: ", mid

        elif(arr[mid] > key):
            high = mid - 1

        else:

            low = mid + 1

    return "Element not found"


arr = [1,2,3,4,5,6,7,8,9]

print(BinarySearch(arr,7))