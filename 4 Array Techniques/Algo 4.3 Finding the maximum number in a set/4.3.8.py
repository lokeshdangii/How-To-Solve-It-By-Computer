arr= [12,1,13,11,64,1,875,34,12,33,1,6,9,875,23]

max = arr[0]
min = arr[0]

for i in range(1,len(arr)):
        if arr[i]<min:
            min = arr[i]
        if arr[i]>max:
            max = arr[i]
        
print("Maximum = ",max)
print("Minimum = ",min)

max_count = 0
min_count = 0

for i in range(0,len(arr)):
        if arr[i] == max:
             max_count +=1
        if arr[i] == min:
             min_count = min_count+1

print("{} occurs {} times".format(max,max_count))
print("{} occurs {} times ".format(min,min_count))

# -------------------------------------------------------------------------    
"""
def maxnum(arr):
    max = arr[0]
    n = 1
    while n<len(arr):
        if arr[n]>max:
            max = arr[n]
        
        n = n+1
    return max

def minnum(arr):
    min = arr[0]
    for i in range(1,len(arr)):
        if arr[i]<min:
            min = arr[i]

    return min

arr1= [12,1,13,11,64,1,875,34,12,33,1,6,9,875,23]
maximum = maxnum(arr1)
minimum = minnum(arr1)
print("Maximum = ",maximum)
print("Minimum = ",minimum)

max_count = 0
min_count = 0

for i in range(0,len(arr1)):
        if arr1[i] == maximum:
             max_count +=1
        if arr1[i] == minimum:
             min_count = min_count+1

print("{} occurs {} times".format(maximum,max_count))
print("{} occurs {} times ".format(minimum,min_count))
        
"""