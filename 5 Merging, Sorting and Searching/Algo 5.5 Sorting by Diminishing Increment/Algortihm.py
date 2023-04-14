arr = [20,35,18,8,14,41,3,39]
n = len(arr)
gap = n
j= n
while gap>=1:
    gap = gap//2
    for j in range(gap,n,1):
        for i in range(j-gap,gap+2,1): 
            no = i
            if arr[i+gap]>arr[i]:
                break
            else:
                arr[i+gap],arr[i] = arr[i],arr[i+gap]
    

print(arr)