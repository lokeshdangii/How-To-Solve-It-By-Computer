def factorial():
    n = int(input("Enter a number : "))
    fseries = 1
    fact = 1
    if n == 0:
        return fseries
    elif n==1:
        return fseries + fact
    elif n<0:
        return "Number less then Zero"
    else:
        for i in range(1,n+1):
            fact = fact * i
            # print("The factorial is : ", fact)
            fseries = fseries + fact
            
            # print("fseries at {} is {}".format(i,fseries))
        # print("The factorial is : ", fact)
    
    return fseries

f = factorial()
print("The sum of the first n terms of the series is :",f)