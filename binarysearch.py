def binarysearch(arr, ele):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = low + high /2
        guess = arr[mid]
        if guess == ele:
            return ele
        
        elif guess > ele:
            high = mid - 1
        
        else:
            low = mid + 1
    
    return None
 


arr1 = [1,2,3,4,5,6,7,8]
binarysearch(arr1,4)

print (binarysearch(arr1,4))
print (binarysearch(arr1,-1))