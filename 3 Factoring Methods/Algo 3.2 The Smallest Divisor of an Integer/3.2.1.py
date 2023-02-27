# Finding smallest Divisor of an given Number 
value = int(input("Enter the value Whose smallest Divisor is Required "))

def smlldiv(x):
   for i in range(2,x+1):
        if(x%i == 0):
            return i
ans = smlldiv(value)        
print("Except 1 ,The smallest divisor of given Number is :" ,ans)