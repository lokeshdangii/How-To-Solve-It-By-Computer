def selectionSort(arr):
    minPos = 0

    for i in range(0,len(arr)-1):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        

        arr[min],arr[i] = arr[i],arr[min]
    

    return arr


arr = [5,4,1,2,3]
print(selectionSort(arr))
