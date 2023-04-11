def bubbleSort(arr):
    n = len(arr)

    for turns in range(0,n-1):
        for j in range(0,n-1-turns):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        
    
    return arr

arr = [5,4,1,3,2]
print(bubbleSort(arr))