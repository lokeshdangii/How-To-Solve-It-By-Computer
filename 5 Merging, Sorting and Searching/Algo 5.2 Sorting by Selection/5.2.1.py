def selectionSortDesc(arr):

    for i in range(0,len(arr)-1):
        max = i
        for j in range(i+1,len(arr)):
            if arr[j] > arr[max]:
                max = j
        

        arr[max],arr[i] = arr[i],arr[max]
    

    return arr


arr = [5,4,1,2,3]
print(selectionSortDesc(arr))
