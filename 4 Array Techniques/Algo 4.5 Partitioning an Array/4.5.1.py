a = [28,26,25,11,16,12,24,29,6,10]

i = 0
j = len(a)-1
x = 17
while i<j:
    if a[i]<=x:
        i = i+1
    elif a[j]>x:
        j = j-1
    else:
        a[i],a[j] = a[j],a[i]
        i = i+1
        j = j-1

print("Array : ",a)