n = int(input("Enter the number of fibonacci no.s to be generated : "))

a = 0
b = 1

print(a,b,end=" ")
# print(b,end=" ")

i = 2
while i < n:
    c = a + b
    print(c,end=" ")
    a = b
    b = c 
    i = i +1
