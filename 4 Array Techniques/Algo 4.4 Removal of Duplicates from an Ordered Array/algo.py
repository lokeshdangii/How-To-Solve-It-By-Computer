arr1 = [22,21,74,23,55,98,98,32,25,56,56,42]
list_arr = [22]
i = 1

while i<len(arr1):
    if arr1[i-1]!=arr1[i]:
        list_arr.append(arr1[i])
    
    i = i+1

print("Array is :",list_arr)