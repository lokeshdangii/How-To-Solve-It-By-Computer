# sieve of eratosthenes
from math import *
def genprimes(n):
    primes = [True]*(n+1)
    primes [0] = False  
    primes [1] = False
    primenumlist = []
    for p in range (2, int(sqrt(n))+1):
        if primes [p] == True:
            for i in range(p*p, n+1,p):
                if primes[i] == False:
                    pass
                else:
                    primes[i] = False
        
        # ------------------------------------------------
        
        # Printing prime numbers 

    for i in range(0, len(primes)):
        if primes[i] == True:
            print (i, end=" ")
            primenumlist.append(i)
    # print("The Prime numbers are : ",primenumlist)
    return primenumlist
          
# -------------------------------------------------------------
n = int(input("Enter n : "))
listofprime = genprimes(n)
print(listofprime)

num = int("Enter a number whose factors is to be compute : ")
