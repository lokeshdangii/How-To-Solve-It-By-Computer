def selectionSort(arr):

    for i in range(0,len(arr)-1):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        

        arr[min],arr[i] = arr[i],arr[min]
        
    
    return arr
    

# arr = [5,4,1,2,3]
arr = [30,12,18,8,14,41,3,39]
# arr = [1,4,12,6,10,8,9]
print(selectionSort(arr))
