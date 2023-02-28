def gcd(a,b):
    r = 0
    while b > 0:
        r = a%b
        a = b
        b =r
        
    return a

a = int(input("Enter a 1st Number : "))
b = int(input("Enter a 2nd Number  : "))
if a>b:
    a,b = b,a

g = gcd(a,b)
print("The gcd is : ",g)
