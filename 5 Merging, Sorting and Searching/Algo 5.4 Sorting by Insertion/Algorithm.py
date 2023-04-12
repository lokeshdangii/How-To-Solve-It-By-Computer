arr = [20,35,18,8,14,41,3,39]
n = len(arr)
min = arr[0]
p = 0
x = int()
j = int()

for i in range(1,n):
    if arr[i]<min:
        min = arr[i]
        p = 0

    arr[p] = arr[1]
    arr[1] = min


for i in range(2,n):
    x = arr[i]
    j = i

    while x<arr[j-1]:
        arr[j] = arr[j-1]
        j = j-1

    arr[j] = x


print(arr)