def arr_order(arr):
    n = len(arr)
    for i in range(0,n-1):
        for j in range(n-1,0,-1):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        # if i == j:
        #break
    print("The array : ",arr)
    return arr

arr = [2,4,6,8,10,12,14,16]
arr_order(arr)