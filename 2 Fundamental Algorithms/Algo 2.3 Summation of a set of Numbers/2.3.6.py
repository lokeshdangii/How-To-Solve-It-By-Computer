# 1 2 4 8 16 32 ....
n = int(input("enter the no. of terms to generate a sequence [1 2 4 8 16 32 ....] : "))
series = []
sum = 1
for i in range(0,n):
    series.append(sum)
    sum = sum + sum

print("series of numbers : ",series)
# sum = sum(series)
# print("the sum of the numbers is : ", sum