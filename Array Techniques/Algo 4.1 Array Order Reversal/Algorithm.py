# Array order reversal

def arrorder(arr):
    n =(len(arr)-1)

    r = int(n/2)
    for i in range(0,r+1):
        temp = arr[i]
        arr[i] = arr[n-i]
        arr[n-i] = temp

    # print("Reverse Array : ",arr)
    return arr

arr = [8,8,2,7,0,3,7,4,4,2]
array = arrorder(arr)
print("Reverse Array : ",array)



