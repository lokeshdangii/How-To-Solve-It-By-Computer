# The minimum and maximum in an array of size n can be found using (3/2)n comparisons instead of 2n comparisons by considering the elements in pairs and comparing the larger element of the pair against the current maximum and the smaller element of the pair against the current minimum. Implement this algorithm
# arr= [12,1,13,11,64,1,875,34,12,33,1,6,9,875,23]

# max = arr[0]
# min = arr[0]

# for i in range(1,len(arr)):
#         if arr[i]<min:
#             min = arr[i]
#         if arr[i]>max:
#             max = arr[i]
    
# print("Maximum = ",max)
# print("Minimum = ",min)


# -----Answer By ChatGPT-----


def find_min_max(arr):
    n = len(arr)
    # Initialize min and max variables
    '''
    if n % 2 == 0:
        # If n is even, compare first two elements to set initial min and max
        if arr[0] > arr[1]:
            max_val = arr[0]
            min_val = arr[1]
        else:
            max_val = arr[1]
            min_val = arr[0]
        i = 2
    else:
        # If n is odd, initialize min and max variables to first element
        max_val = arr[0]
        min_val = arr[0]
        i = 1
        '''
    i = 0
    max_val = arr[0]
    min_val = arr[0]
    # Compare elements in pairs
    while i < n-1:
        if arr[i] > arr[i+1]:
            if arr[i] > max_val:
                max_val = arr[i]
            if arr[i+1] < min_val:
                min_val = arr[i+1]
        else:
            if arr[i+1] > max_val:
                max_val = arr[i+1]
            if arr[i] < min_val:
                min_val = arr[i]
        i += 2

    return min_val, max_val


arr= [12,1,13,11,64,1,875,34,12,33,1,6,9,875,23]
min_max = find_min_max(arr)
print(min_max)