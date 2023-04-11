def bubbleSort(arr):
    n = len(arr)
    for turns in range(0,n-1):
        for j in range(0,n-1-turns):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                count = count + 1
        
    return arr

# arr = [5,4,1,3,2]
arr = [30,12,18,8,14,41,3,39]
print(bubbleSort(arr))