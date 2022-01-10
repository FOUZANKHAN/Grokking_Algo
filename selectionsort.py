def findsmallest(arr):
    smallest = arr[0]
    smallestindex = 0
    for i in range(0,len(arr)-1):
        if arr[i]<smallest:
            smallest = arr[i]
            smallestindex = i
    return smallestindex

def selectionsort(arr):
    newarr = []
    for i in range(0,len(arr)-1):
        smallestnumber = findsmallest(arr)
        newarr.append(arr.pop(smallestnumber))
    return newarr

arr = t

print(selectionsort(arr))