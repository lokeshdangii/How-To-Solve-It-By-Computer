# The minimum and maximum in an array of size n can be found using (3/2)n comparisons instead of 2n comparisons by considering the elements in pairs and comparing the larger element of the pair against the current maximum and the smaller element of the pair against the current minimum. Implement this algorithm
arr= [12,1,13,11,64,1,875,34,12,33,1,6,9,875,23]

max = arr[0]
min = arr[0]

for i in range(1,len(arr)):
        if arr[i]<min:
            min = arr[i]
        if arr[i]>max:
            max = arr[i]
    
print("Maximum = ",max)
print("Minimum = ",min)


# ------------------------------------------------------------------------


def find_min_max(arr):
    
    # Initialize min and max variables
    i = 0
    max_val = arr[0]
    min_val = arr[0]
    # Compare elements in pairs
    while i < len(arr)-1:
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
    
    # Handle the case where there is an odd number of elements
    if len(arr) % 2 != 0:
        if arr[-1] < min_val:
            min_val = arr[-1]
        elif arr[-1] > max_val:
            max_val = arr[-1]

    return min_val, max_val


arr= [12,1,13,11,64,1,875,34,12,33,1,6,9,875,23]
min_max = find_min_max(arr)
print(min_max)