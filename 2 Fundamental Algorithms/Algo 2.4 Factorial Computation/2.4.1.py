i = int(input("Enter number :"))
fact = 1
if i == 0 or i ==1:
	print("{} is factorial of {}".format(fact,i))
else:
	for j in range(1,i+1):
		fact = fact*j
	print("{} is factorial of 1/{}". format(fact,i))
	
oneUponNFact = 1/fact
print(oneUponNFact)