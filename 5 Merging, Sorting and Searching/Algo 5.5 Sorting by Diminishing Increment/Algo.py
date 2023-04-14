# a = [20,35,18,8,14,41,3,39]
a = [15,19,20,38,24,41,30,31,12]
n = len(a)
gap = n//2

while gap>=1:
    j = gap
    for i in range(0,n-gap):
        if a[i]>a[j]:
            a[i],a[j] = a[j],a[i]
        print("for gap = {} and i = {} j is {}".format(gap,i,j))
        j = j+1
    gap = gap//2
        
    
    
    


print(a)