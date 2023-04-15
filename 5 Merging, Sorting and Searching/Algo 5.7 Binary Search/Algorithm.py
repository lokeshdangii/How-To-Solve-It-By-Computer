
def binarySearch(arr,ele):
    n = len(arr)
    lower = 0
    upper = n-1
    

    while lower < upper :
        middle = (lower+upper)//2

        if ele > arr[middle]:
            lower = middle +1 
            if arr[lower] == ele:
                return lower
        else:
            upper = middle
        
    return -1

arr = [10,12,20,23,27,30,31,39,42,44,45,49,57,63]
ele = 42
print(binarySearch(arr,ele))

