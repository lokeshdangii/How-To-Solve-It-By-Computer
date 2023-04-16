def binarySearch(arr,ele):
    lower = 0
    upper = len(arr)-1
    

    while lower < upper-1 :
        middle = (lower+upper)//2
        
        if arr[middle] == ele:
            return middle
        elif ele>arr[middle]:
            lower = middle+1
        else:
            upper = middle-1
        
    return -1

arr = [10,12,20,23,27,30,31,39,42,44,45,49,57,63]
arr1 = [1, 3, 5, 7, 9]
ele = 5
print(binarySearch(arr1,ele))