def minnum(arr):
    min = 0
    n = 0
    while n<len(arr):
        if arr[n]<min:
            min = arr[n]
        
        n = n+1
    return min



arr1= [12,12,65,13,11,64,24,875,34,2334,-12,33,1,6,9,232,23]
minnumber = minnum(arr1)
print("The minimum number in a set is : ",minnumber)