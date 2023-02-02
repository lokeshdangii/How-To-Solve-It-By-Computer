numlist = []
n = int(input("Enter the no. of nums needed to sum: "))

for i in range(0,n):
    ele = int(input("Enter the number:"))
    numlist.append(ele)

print("the list of numbers : ", numlist)

sum = 0
for i in numlist:
    sum = sum + (i*i)

print("The sum of sq. of numbers is: ",sum)
# avg = sum/n
# print("the average of n numbers is : ",avg)
