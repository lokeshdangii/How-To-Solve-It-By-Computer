arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd = []
even = []
for i in range(len(arr)):
    if i%2 ==1:
        odd.append(arr[i])
    else:
        even.append(arr[i])

new_arr = odd + even

for i in range(len(arr)):
    arr[i] = new_arr[i]

print("Array :",arr)


# Input: An array A with n elements

# 1. Initialize two pointers i and j to the first and second elements of A, respectively.
# 2. While i < n and j < n, do the following:
#     a. If i is odd and j is even, swap A[i] and A[j].
#     b. If i is even, increment i.
#     c. If j is odd or j is less than i, increment j.
# 3. Return the rearranged array A.
