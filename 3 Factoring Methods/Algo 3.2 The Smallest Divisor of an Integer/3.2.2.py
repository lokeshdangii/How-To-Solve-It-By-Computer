def smalldiv(num):
    divisors = []
    for i in range(2,num+1):
        if num%i == 0:
            divisors.append(i)
    
    print("The list of all exact divisors of a given positive integer is : ",divisors)


num = int(input("Enter a positive integer n : "))
smalldiv(num)