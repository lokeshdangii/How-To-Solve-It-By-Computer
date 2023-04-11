def exchangeSort(arr):
    n = len(arr)

    sorted = False
    i = 0
    count = 0

    while i < n and not sorted:

        sorted = True
        for j in range(0,n-1-i):
            if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                    sorted = False
                    count = count+1
        i = i+1
            
    # print("Array after sorting : ",arr)
    print("Count :",count)
    return arr

# --------------------------------------------------------------------------------

def selectionSort(arr):
    count = 0
    for i in range(0,len(arr)-1):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        

        arr[min],arr[i] = arr[i],arr[min]
        count = count+1
    
    print("count : ",count)
    return arr

# arr = [1,4,12,6,10,8,9]
arr = [30,12,18,8,14,41,3,39]
# arr = [5,4,1,2,3]
print(exchangeSort(arr))
print(selectionSort(arr))
