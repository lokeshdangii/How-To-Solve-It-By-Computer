# arr = [5,4,1,2,3]
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
# arr = [1,2,9,4,7,3,11,8,14,6]
seq_len = []
count = 0
for i in range(1,len(arr)):
    count = 0
    for j in range(1,i+1):
        if arr[i]>arr[j-1] and arr[i]>arr[j] and arr[i]>arr[j+1]:
            count +=1

    # print("count for {} index = {}".format(i,count))    
    seq_len.append(count)
     

print(seq_len)
longest = max(seq_len)
print("The length of longest monotone increasing subsequence is :",longest)