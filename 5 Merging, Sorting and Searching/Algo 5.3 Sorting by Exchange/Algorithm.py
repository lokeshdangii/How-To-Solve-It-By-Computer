# Sorting by Exchange


def exchangeSort(arr):
    n = len(arr)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
    
    print("Array after sorting : ",arr)
    return arr


'''
# def exchangeSort(arr):
#     n = len(arr)

#     indicator = False

#     for i in range(0,n-1):
#         while indicator == False:
#             for j in range(0,n-1-i):
#                 if arr[j]>arr[j+1]:
#                     arr[j],arr[j+1] = arr[j+1],arr[j]
#                     print("Array after {} pass and j = {} : {}".format(i,j,arr))
#                     indicator = False
#                 else:
#                     indicator = True
            
#     print("Array after sorting : ",arr)
#     return arr
'''

# arr = [1,4,6,10,8,9]
arr = [30,12,18,8,14,41,3,39]
print(exchangeSort(arr))
