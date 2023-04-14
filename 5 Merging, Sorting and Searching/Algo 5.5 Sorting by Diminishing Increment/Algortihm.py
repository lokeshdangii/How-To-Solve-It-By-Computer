arr = [20,35,18,8,14,41,3,39]
n = len(arr)
inc = n
passs = 0
while inc > 1:
    inc = inc//2
    passs = passs+1
    for i in range(0,inc):
        if arr[i]>arr[n-inc+i]:
            arr[i],arr[n-inc] = arr[n-inc],arr[i]
    print("Array after {} pass and {} distance is {} ".format(passs,inc,arr))

print(arr)