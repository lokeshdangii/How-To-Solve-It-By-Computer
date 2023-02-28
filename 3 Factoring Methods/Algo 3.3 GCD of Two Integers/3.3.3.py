def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

n = int(input("Enter a number of integers  :"))
list1 = []
# for i in range(1,n+1):
#     g = gcd(n,n-1)
#     list.append(g)

while n > 0:
    g = gcd(n,n-1)
    list1.append(g)
    n = n-1

print("GCD of n numbers is : ",list1)