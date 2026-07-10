def rotate(arr,k):
    k %= len(arr)
    def reverse(left,right):
        while left < right :
            arr[left],arr[right] = arr[right],arr[left]
            left +=1
            right -=1
    
    reverse(0,k-1)
    reverse(k,len(arr)-1)
    reverse(0,len(arr)-1)
    
arr = [1,2,3,4,5,6,7]
k = 3 
rotate(arr,k)
print(arr)