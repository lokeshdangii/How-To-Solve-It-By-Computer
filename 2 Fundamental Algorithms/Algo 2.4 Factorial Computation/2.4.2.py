# For a given x and given n, design an algorithm to compute x^n/n!.

def xPowern(x):
	mult = x
	for i in range(1,n):
		mult = mult *x
	return mult

def factorial(n):
	fact = 1
	if(n ==1 or n == 0):
		return fact
	elif n<0:
		return -1
	else:
		for i in range(1,n+1):
			fact = fact * i
		return fact

x = int(input("enter x :"))
n = int(input("Enet n :"))
xPowern_upon_Factorialn = xPowern(x)/factorial(n)

print("{} power {} = {}.".format(x,n,xPowern(x)))
print("{} is factorial of {}". format(factorial(n),n))
print("{} upon {} is {}.".format(xPowern(x),factorial(n),xPowern_upon_Factorialn))