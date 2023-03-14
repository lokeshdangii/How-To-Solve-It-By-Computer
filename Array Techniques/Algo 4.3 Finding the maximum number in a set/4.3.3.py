def maxnum(arr):
    max = arr[0]
    n = 1
    occurence = []
    while n<len(arr):
        if arr[n]>max:
            max = arr[n]
        
        n = n+1
    
    for i in range(0,len(arr)):
        if arr[i] == max:
            occurence.append(i)

    first_occurence = occurence[0]
    last_occurence = occurence.pop()   
    # print("occurence of maximum : ",occurence)
    print("First Occurence : ",first_occurence)
    print("Last Occurence : ",last_occurence)
    




arr1= [12,12,232,13,11,64,232,85,34,56,12,33,1,6,9,232,23]
maxnum(arr1)
# print("The maximum number in a set is : ",maxnumber)