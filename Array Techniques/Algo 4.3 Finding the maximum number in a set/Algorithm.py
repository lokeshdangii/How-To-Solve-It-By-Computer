def maxnum(arr):
    max = arr[0]
    n = 1
    while n<len(arr):
        if arr[n]>max:
            max = arr[n]
        
        n = n+1
    return max



arr1= [12,12,65,13,11,64,24,875,34,2334,12,33,1,6,9,232,23]
maxnumber = maxnum(arr1)
print("The maximum number in a set is : ",maxnumber)