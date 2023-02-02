# Design an algorithm that reads a list of numbers and makes a count of the number of negatives and the number of non negative members in the set

listofnum = []
n = int(input("enter no. of elments want to store in list:"))

for i in range(0,n):
	ele = int(input("Enter a number:"))
	listofnum.append(ele)

print("the list of number : ", listofnum)

negativecount = 0
positivecount = 0

for i in listofnum:
	if i<0:
		negativecount = negativecount+1
	else:
		positivecount = positivecount +1
	
print("The count of Positive number and Negative number are {} and {}".format(positivecount,negativecount))
