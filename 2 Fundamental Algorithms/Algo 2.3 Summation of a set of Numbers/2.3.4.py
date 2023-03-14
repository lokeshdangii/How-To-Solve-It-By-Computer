numlist = []
n = int(input("Enter the no. of nums needed to sum: "))

for i in range(0,n):
    ele = int(input("Enter the number:"))
    numlist.append(ele)

print("the list of numbers : ", numlist)

sum = 0
for i in numlist:
    sum = sum + (1/numlist[i])

print("The sum of numbers is: ",sum)
harmonicmean = n/sum
print("The Harmonic mean of n data values is : ", harmonicmean)
