# 
def power(n,x):

    power_sequnce = x
    product = 1

    while n>0:
        if n%2 == 1:
            product = product * power_sequnce
    
        n = int(n/2)
        power_sequnce = power_sequnce* power_sequnce

    return product


n = int(input("Enter a power :"))
x = int(input("Enter a integer to be raised to power n : "))
Answer = power(n,x)
print("Integer raised after power n : ",Answer)