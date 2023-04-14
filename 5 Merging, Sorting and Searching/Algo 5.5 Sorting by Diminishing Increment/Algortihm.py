arr = [20,35,18,8,14,41,3,39]
n = len(arr)
gap = n

while gap>=1:
    gap = gap//2
    for j in range(gap,n,1):
        for i in range(j-gap,0,1): #i-gap
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
            else:
                break
    

print(arr)