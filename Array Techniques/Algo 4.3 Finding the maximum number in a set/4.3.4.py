# import math

def absdiff(arr):
    diff_array = []
    for i in range(0,len(arr)-1):
        diff = abs(arr[i]-arr[i+1])
        diff_array.append(diff)
    
    return diff_array

def maxAbsDiffer(arr):
    max = arr[0]
    n = 1
    while n<len(arr):
        if arr[n]>max:
            max = arr[n]
        
        n = n+1
    return max

arr1= [12,12,65,13,11,64,24,875,34,23,12,33,1,6,9,232,23]
abs_diff = absdiff(arr1)
maximum = maxAbsDiffer(abs_diff)
print("Maximum Absolute difference between the adjacent pair of elements in an array : ",maximum)
