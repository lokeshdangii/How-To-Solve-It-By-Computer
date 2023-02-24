n = int(input("Enter the number of fibonacci no.s to be generated : "))

a = 0
b = 1
print(a,end=" ")
print(b,end=" ")
i = 2
while i < n:
    i = i +2
    a = a+b
    b = a+b
    print(a,end=" ")
    print(b,end=" ")
    

