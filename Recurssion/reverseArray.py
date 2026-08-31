def rev(arr,l,r):

    if l > r:
        return arr
    
    arr[l],arr[r]= arr[r],arr[l]
    l +=1
    r -=1
    return rev(arr,l,r)
    


arr = [1,2,3,4,5]

print(rev(arr,0,4))