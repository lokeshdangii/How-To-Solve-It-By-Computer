# Removal of Duplicates from an ordered array 
arr1 = [12,34,343,13,65,126,44,44,21,34,31,24,24,34]
n = len(arr1)
j = 0
for i in range(1,len(arr1)):
    if arr1[i-1] != arr1[i]:
        arr1[j] =arr1[i-1]
        j+=1

print(arr1)
for i in range(0,j):
    print(arr1[i],end=" ")




# this logic is not good for the unsorted array....!