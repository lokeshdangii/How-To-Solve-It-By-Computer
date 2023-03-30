# finding the kth Smallest element

a = [26,28,25,11,16,12,24,29,6,10]
l = 0
u = len(a)-1
k = 7

while l<u:
    i = l
    j = u
    x = a[k]

    while i<=k and j>=k:
        while a[i]<x:
            i = i+1
        while a[j]>x:
            j = j-1
        while i<=j:
            a[i],a[j] = a[j],[a[i]]
            i = i+1
            j = j-1
            # while a[i]<x:
            #     i = i+1
            # while a[j]>x:
            #     j = j-1
        if j<k:
            l = i
        if i>k:
            u = j

print("Array : ",a)
for ele in range(0,k+1):
    print(a[ele],end=" ")