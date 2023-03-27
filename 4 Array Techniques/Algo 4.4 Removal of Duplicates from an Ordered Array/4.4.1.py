# Remove from an ordered list all numbers that occurs more than once.

arr1 = [2,3,4,5,2,4,2,2,2,2,2,4,4,4,4,4,4]
print(len(arr1))
for i in range(0,len(arr1)):
    for j in range(i+1,len(arr1)-1):
        if arr1[i] == arr1[j]:
            arr1.remove(arr1[j])
        if i==5:
            break
        
print("Array after duplicay removal will be : ",arr1)









# list1 = [2,2,3,4,66,4,6,4,4,4,4,4,4,2,4,4,4]
# cnt = list1.count(4)
# print(cnt)