# s = 1+2+3+......
n = int(input("enter the no. of terms to be sum up : "))
sum = 0
series = []
for i in range(1,n+1):
    sum = sum + i
    series.append(i)

print("series of numbers : ",series)

print("the sum of the numbers is : ", sum)