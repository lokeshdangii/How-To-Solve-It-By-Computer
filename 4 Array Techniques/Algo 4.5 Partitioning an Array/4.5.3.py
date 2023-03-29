# The problem of Dutch National Flag
# The problem is also sometimes called the 3-way partitioning problem or the flag of the United States problem.

def dnf_partition(a):
    low = 0
    i = 0
    j = len(a)-1

    
    while i<j:
       
        if a[i]==0:
           a[low],a[i]= a[i],a[low]
           low = low+1
           i = i+1
        elif a[i] ==1:
            i = i+1
        else:
            a[i],a[j] = a[i],a[j]
            j = j-1

    return a


arr = [0,1,2,0,1,2]
x = 1
result = dnf_partition(arr)
print("Result = ",result)