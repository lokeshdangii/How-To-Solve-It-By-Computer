from math import *

def factors(n):
    factlist = []
    if n == 1:
        print("Invalid")

    for i in range(2,int(sqrt(n)),1):
        while n%i == 0:
            # print(i,end=" ")
            factlist.append(i)
            n = n/i
        
    if n>1:
        # print(n,end=" ")
        factlist.append(int(n))
    return factlist

num = int(input("Enter a number : "))
fact = factors(num)
print("The factors of a number are : ",fact)