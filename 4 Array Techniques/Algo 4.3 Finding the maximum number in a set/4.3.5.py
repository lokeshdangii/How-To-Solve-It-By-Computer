def secondMax(arr):
    max = arr[0]
    n = 1
    while n<len(arr):
        if arr[n]>max:
            max = arr[n]
        
        n = n+1
    
    second_max = arr[0]
    print("Second Max = ",second_max)
    for i in range(1,len(arr)):
        if arr[i] < max and arr[i] >second_max :
            second_max = arr[i]

    print("The maximum element of array is : ",max)
    print("Second max element of array : ",second_max)   
    return second_max 
    

arr1= [12,12,65,13,11,64,24,875,34,2334,12,33,1,6,9,232,23]
secondMax(arr1)
