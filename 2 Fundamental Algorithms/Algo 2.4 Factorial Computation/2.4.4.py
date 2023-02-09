# Design an algorithm to determine whether or not a number n is a fatorial number

# ---------------function-----------------

def fct(n): 
    fact=1 
    i=1 
    while(fact<n): 
        fact=fact*i 
        if(fact==n): 
            factlist.append(i)
            return i 
            break 
        else: 
            i=i+1 
    factlist.append(-1)
    return -1 


n = int(input("Enter no. of factorial to test :"))
nlist = []
factlist = []


for i in range(n):
    num = int(input("enter a number :"))
    nlist.append(num)


for i in range(0,len(nlist)):
    fct(nlist[i])

print("\nlist of no. :",nlist)
print("\nlist of factorial of n: ",factlist)
maxFact = max(factlist)
print("\nlargest factorial number : ",maxFact)

