def absdiff(arr):
    max = arr[0]
    n = 1
    abs_diff = []
    while n<len(arr):
        if arr[n]>max:
            max = arr[n]
        
        n = n+1
    for i in range(0,len(arr)):
        abs_diff.append(max-arr[i])
    print("The maximum element of array is : ",max)
    print("The maximum absolute difference between adjacent pairs of elements in an array : ",abs_diff)
    return abs_diff


arr1= [12,12,65,13,11,64,24,875,34,23,12,33,1,6,9,232,23]
difference = absdiff(arr1)
