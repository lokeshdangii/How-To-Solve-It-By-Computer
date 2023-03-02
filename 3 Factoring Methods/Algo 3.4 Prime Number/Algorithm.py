# sieve of eratosthenes
from math import *
def genprimes(n):
        primes = [True]*(n+1)
        primes [0] = False  
        primes [1] = False
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
          

n = int(input("Enter n : "))
genprimes(n)