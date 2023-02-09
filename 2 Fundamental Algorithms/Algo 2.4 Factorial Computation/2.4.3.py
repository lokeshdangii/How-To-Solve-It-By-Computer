# Design an algorithm to determine whether or not a number n is a fatorial number

def fct(n): 
    fact=1 
    i=1 
    while(fact<n): 
        fact=fact*i 
        if(fact==n): 
            return i 
            break 
        else: 
            i=i+1 
    return("Not found") 

n=int(input("Enter n:"))
print ("Factorial of a no is ",fct(n))