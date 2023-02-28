# Algoritha for the GCD of two buabers 

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
    

a = int(input("Enter a 1st Number : "))
b = int(input("Enter a 2nd Number  : "))
if a>b:
    a,b = b,a
gcd1 = gcd(a,b)
print("GCD = ",gcd1)