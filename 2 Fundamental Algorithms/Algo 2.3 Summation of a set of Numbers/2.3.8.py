# 1-3+5-7+9-....

n = int(input("enter no. of terms : "))
sum = 1
series = [1]

for i in range(0,n):
    sum = sum +2
    if i%2==0:
        series.append(-(sum))
    else:
        series.append(sum)

print("series of sequence is  : ",series )