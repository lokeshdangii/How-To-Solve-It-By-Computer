# The problem of Dutch National Flag
# The problem is also sometimes called the 3-way partitioning problem or the flag of the United States problem.

def dnf_partition(arr):
    low = 0
    mid = 0
    high = len(arr)-1

    while mid<=high:
        if arr[mid] == 0:
            arr[mid],arr[low] = arr[low],arr[mid]
            mid = mid + 1
            low = low + 1
        elif arr[mid] ==1:
            mid = mid +1
        else :
            arr[mid], arr[high] = arr[high],arr[mid]
            high=high-1

    return arr



a = [0,1,2,0,1,2]
result = dnf_partition(a)
print("Result = ",result)