arr = [20,35,18,8,14,41,3,39]
n = len(arr)
gap = n//2

while gap>=1:
    
    for j in range(gap,n,1):
        for i in range(0,j,1): 
            no = i
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
            else:
                break
    gap = gap//2
    

print(arr)