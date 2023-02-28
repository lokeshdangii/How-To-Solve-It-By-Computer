
def gcd(a,b):
    for i in range(1,a):
        r = a%b
        a = b
        b =r
        if r == 0:
            break
    return a

a = int(input("Enter a 1st Number : "))
b = int(input("Enter a 2nd Number  : "))
if a>b:
    a,b = b,a

gcd1 = gcd(a,b)
print("The GCD of {} and {} is : {}".format(a,b,gcd1))