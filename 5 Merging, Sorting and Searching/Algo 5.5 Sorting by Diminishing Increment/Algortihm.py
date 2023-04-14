# Shell Sort/ Sorting by deminishing increment 

def shellSort(arr):
    n = len(arr)
    gap = n//2

    while gap>=1:

        for j in range(gap,n,1):
            for i in range(j-gap,-1,-gap): 
                if arr[i+gap]>arr[i]:
                    break
                else:
                    arr[i+gap],arr[i] = arr[i],arr[i+gap]
        gap = gap//2

    print(arr)
    return arr

arr = [20,35,18,8,14,41,3,39]
a = [14,18,19,37,23,40,29,30,11]
shellSort(a)
