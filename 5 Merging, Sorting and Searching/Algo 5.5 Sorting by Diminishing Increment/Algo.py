
def shellSort(a):
    n = len(a)
    gap = n//2

    while gap>=1:
        j = gap
        for i in range(0,n-gap):
            if a[i]>a[j]:
                # print("for gap {} and i = {} j is {} and swap of {} with {}".format(gap,i,j,a[i],a[j]))
                a[i],a[j] = a[j],a[i]
            j = j+1
        
        # print("\n","array after gap {} and swaping is {}".format(gap,a),"\n")

        gap = gap//2
            
    print("Array after sorting : ",a)

    # for i in range(0,n-1):
    #     if a[i]>a[i+1]:
    #         a[i],a[i+1] = a[i+1],a[i]
    # print("array after one more swap : ",a)


list = [12,34,78,54,2,3]
shellSort(list)