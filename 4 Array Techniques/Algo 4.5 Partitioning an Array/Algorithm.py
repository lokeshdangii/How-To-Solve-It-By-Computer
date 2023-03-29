# Algorithm to partition the elements into two subsets such that elements <=x in one subset and elements>x are in other subsets
def partition_array(a,x):
    i = 0
    j = len(a)-1

    while i<j and a[i]<=x:
        i = i+1
    while i<j and a[j]>x:
        j = j-1
 
    while i<j:
        a[i],a[j] = a[j],a[i]
        i = i+1
        j = j-1
        while a[i]<=x:
            i = i+1
        while a[j]>x:
            j = j-1

    return a


a = [28,26,25,11,16,12,24,29,6,10]
arr = [15,2,3,18,20,4,25,18,8,19,22]
x = 17
result = partition_array(arr,x)
print("The array after partition :",result)
