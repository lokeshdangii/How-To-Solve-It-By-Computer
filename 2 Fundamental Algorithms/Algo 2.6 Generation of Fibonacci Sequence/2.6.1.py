# 0 1 1 2 3 5 8 13.....

def fibonacci(a,b):
    c = a+b
    return c


a = int(input("Enter a Fibonacci number : "))
b = int(input("Enter another consecutive Fibonacci number : "))
result = fibonacci(a,b)
print("The next fibonacci number is : ",result)
