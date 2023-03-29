# Delete from an ordered array all elements that occur more than k times

def remove_elements_greater_than_k(arr, k):
    freq_dict = {}
    new_arr = []
    
    for i in range(len(arr)):
        if arr[i] not in freq_dict:
            freq_dict[arr[i]] = 1
        else:
            freq_dict[arr[i]] += 1
    print("Dictionary = ",freq_dict)
    
    for key, value in freq_dict.items():
        if value <= k:
            new_arr += [key] * value
            print("array in loop ;-",new_arr)
    
    return new_arr


arr = [1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5,6,7,8,8,10,14,16,18,18,19,20,20]
result = remove_elements_greater_than_k(arr,2)
# print("The array after duplicate removal :",result)
