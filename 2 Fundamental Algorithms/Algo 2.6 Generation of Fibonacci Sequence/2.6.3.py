n = int(input("Enter the no. of terms to be generate : "))

a = 0
b = 1
c = 1

print(a,b,c,end=" ")
i = 3
'''
while i <n:
    next = a+b+c
    print(next,end=" ")
    a= b
    b = c
    c = next
    i = i +1
'''

while i < n:
    a = a+b+c
    b = a+b+c
    c = a+b+c
    print(a,b,c,end=" ")
    i = i +3

