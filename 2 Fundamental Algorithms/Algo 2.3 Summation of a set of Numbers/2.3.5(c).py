# 1 + 1/2 + 1/3 +.....

n = int(input("enter the no. of terms to be sum up : "))
series = []
ele = 0
for i in range(1,n+1):
    ele = 1/i
    series.append(ele)

print("series of numbers : ",series)
sum = sum(series)
print("the sum of the numbers is : ", sum)