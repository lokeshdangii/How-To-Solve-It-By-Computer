def selectionSort(arr):

    for i in range(0,len(arr)-1):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
                arr[min],arr[i] = arr[i],arr[min]
            elif arr[j] == arr[min]:
                arr.remove(arr[min])
            else:
                pass
            

        # arr[min],arr[i] = arr[i],arr[min]
    

    return arr


arr = [5,15,18,3,19,15,4,8,6,0]
print(selectionSort(arr))
