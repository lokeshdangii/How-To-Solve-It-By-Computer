a = [1,2,9,4,7,3,11,8,14,6]
length = [0]*100
length[0] = 1
pmax = 1
maxlength = 1
maxj = int()
current = 0

for i in range(1,len(a)+1):
    current = a[i]
    if current<a[pmax]:
        maxj = 1
    
    for j in range(0,i-1):
        if a[j]<current:
            if maxj < length[j]:
                maxj = length[j]
        length[i] = maxj + 1

        if length[i]>maxlength:
            maxlength = maxlength+1
            pmax = i
    else:
        maxlength = maxlength + 1
        length[i] = maxlength
        pmax = i
    
print("longest monotone subsequence :",maxlength)