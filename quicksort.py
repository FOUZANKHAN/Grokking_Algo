def quicksort(arr):
    if(len(arr)<2):
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1: ] if i<=pivot]
        more = [i for i in arr[1:] if i> pivot]
        return quicksort(less) + [pivot] + quicksort(more)
        
arr = [7,9,2,3,5,61,0,54,11,76,3]
            
print(quicksort(arr))