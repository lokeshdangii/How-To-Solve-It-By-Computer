def maxNumCount(arr):
    max = arr[0]
    count = 1
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
            count = 1
        elif arr[i] == max:
            count += 1
    return count   

arr1= [12,12,65,2334,13,11,64,24,875,34,2334,12,33,1,6,2334,9,232,23]
maxcount = maxNumCount(arr1)
print("The count of maximum number in a set is : ",maxcount)