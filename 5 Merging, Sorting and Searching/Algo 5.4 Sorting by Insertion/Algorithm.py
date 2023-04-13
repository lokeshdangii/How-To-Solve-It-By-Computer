def insertionSort(arr):
    
    for i in range(1,len(arr)):
        x = arr[i]
        j = i-1

        while j >=0 and arr[j] > x:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = x

    print(arr)


arr = [20,35,18,8,14,41,3,39]
insertionSort(arr)

