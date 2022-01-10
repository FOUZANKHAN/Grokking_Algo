def sum(arr):
    if(len(arr) == 1):
        return arr[0]
    else:
        print(arr)
        return arr[0] + sum(arr[1:])

arr = [3,4,6,8,9,1,2,32,3]

print(sum(arr))