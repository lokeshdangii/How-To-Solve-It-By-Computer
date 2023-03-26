# Removal of Duplicates from an ordered array 
arr1 = [12,34,343,13,65,126,44,44,21,34,31,24,24,34]
n = len(arr1)
print(n)
j = int()
i = 1
while arr1[i-1] == arr1[i] and i<n:
    i = i+1
    if arr1[i-1] == arr1[i]:
        j = i-1

while i<n:
    i = i+1
    if arr1[i-1] == arr1[i]:
        j = j+1
        arr1[j] = arr1[i]
    
print("The array is : ", arr1)