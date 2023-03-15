def rearrange_array(arr):
    n = len(arr)
    i = 1
    j = n - 1
    
    while i < j:
        if arr[i] % 2 == 0:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
        else:
            i += 1
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
array = rearrange_array(arr)
print(array)