# Remove from an ordered list all numbers that occurs more than once.
def remove_duplicate(arr):
    new_arr = []

    for i in range(1,len(arr1)):
        if arr1[i-1]!=arr1[i]:
            new_arr.append(arr1[i])
        
    return new_arr

arr1 = [1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5,6,7,8,8,10,14,16,18,18,19,20,20]
result = remove_duplicate(arr1)
print("The array after duplicate removal :",result)








# list1 = [2,2,3,4,66,4,6,4,4,4,4,4,4,2,4,4,4]
# cnt = list1.count(4)
# print(cnt)