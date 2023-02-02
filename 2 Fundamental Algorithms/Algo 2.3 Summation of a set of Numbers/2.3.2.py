numlist = []
n = int(input("Enter the no. of nums needed to sum: "))

for i in range(0,n):
    ele = int(input("Enter the number:"))
    numlist.append(ele)

print("the list of numbers : ", numlist)

sum = numlist[0]
for i in range(1,n):
    sum = sum + numlist[i]

print("The sum of numbers is: ",sum)
# avg = sum/n
# print("the average of n numbers is : ",avg)
