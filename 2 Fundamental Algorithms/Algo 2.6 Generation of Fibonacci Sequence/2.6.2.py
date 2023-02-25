# Lucas Series = 1 3  4  7 11 18  29 ....
n = int(input("Enter the n : "))

a = 1
b = 3
print(a,b,end=" ")
i = 2
while i < n:
    i = i + 2
    a = a+b
    b = a+b
    print(a,end=" ")
    print(b,end=" ")