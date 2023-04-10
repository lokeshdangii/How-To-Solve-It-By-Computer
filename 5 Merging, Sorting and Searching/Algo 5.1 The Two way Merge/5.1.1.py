a = [2,8,15,18] 
b = [5,9,12,17,16]
c = []

i,j = 0,0

while i<len(a) and j <len(b):
    if a[i]<=b[j]:
        c.append(a[i])
        i = i+1
    else:
        c.append(b[j])
        j = j+1
    
print(c)