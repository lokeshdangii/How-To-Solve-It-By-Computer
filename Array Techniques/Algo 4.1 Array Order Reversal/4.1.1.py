# what happens if exchange process continues for n steps rather than [n/2] steps ?

def array_order(arr):
    n =(len(arr)-1)

    r = int(n/2)
    for i in range(0,n+1):
        temp = arr[i]
        arr[i] = arr[n-i]
        arr[n-i] = temp

    # print("The array is : ",arr)
    return arr


arr = [8,8,2,7,0,3,7,4,4,2]
array = array_order(arr)
print("Array : ",array)


# When the exchange process continues for n steps rather than [n/2] steps, The returned array will be the original array 
