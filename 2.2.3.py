listofnum = []
n = int(input("enter no. of elments want to store in list:"))

for i in range(0,n):
	ele = int(input("Enter a number:"))
	listofnum.append(ele)

print("the list of number : ", listofnum)

count = len(listofnum)

for i in listofnum:
	# Since 50 is considered as passing mark
	if i<50: 
		count = count-1
	
print("The total students passed are: ",count)