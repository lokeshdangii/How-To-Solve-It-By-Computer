
def arr_order(arr):
    n = len(arr)-1
    i = 0
    j = n
    while i<j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i = i+1
        j = j-1
    
    print("The array : ",arr)
    return arr

arr = [2,4,6,8,10,12,14,16]
arr_order(arr)