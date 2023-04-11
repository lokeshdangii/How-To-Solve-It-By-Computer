def exchangeSort(arr):
    n = len(arr)

    sorted = False
    i = 0

    while i < n and not sorted:

        sorted = True
        for j in range(0,n-1-i):
            if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                    sorted = False
            print("Array after {} pass and j = {} : {}".format(i,j,arr))
                    
        
        i = i+1
            
    print("Array after sorting : ",arr)
    return arr

arr = [1,4,12,6,10,8,9]
# arr = [30,12,18,8,14,41,3,39]
print(exchangeSort(arr))
