
def binarySearch(arr):
    n = len(arr)
    x = 44
    lower = arr[0]
    upper = arr[n-1]
    middle = int()

    while arr[middle] == x or lower > upper :
        middle = (lower+upper)//2
        # if arr[middle] == x:
        #     return middle
        if x>arr[middle]:
            lower = middle+1
        else:
            upper = middle-1
        
    # return -1

arr = [10,12,20,23,27,30,31,39,42,44,45,49,57,63,70]
result = binarySearch(arr)
print(result)

