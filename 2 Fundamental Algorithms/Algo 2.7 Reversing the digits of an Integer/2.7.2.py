n = int(input("Enter a number : "))
sum = 0

while n > 0:
    rem = n%10
    sum = sum + rem
    n = int(n/10)
    
print("The sum of digits of an integers is : ",sum)