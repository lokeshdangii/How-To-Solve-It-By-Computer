n = int(input("enter the no. of terms : "))
num = 1
series = []

for i in range(0,n):
    if i%2==0:
        series.append(num)
    else:
        series.append(-(num))

print("series of sequence is  : ",series )