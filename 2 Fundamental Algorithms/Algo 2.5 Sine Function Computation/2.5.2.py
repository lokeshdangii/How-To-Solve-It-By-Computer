numerator = 1
n = int(input("Enter a number :"))
e = 0
fact = 1

for i in range(0,n+1):
    if i == 0:
        fact = 1
        e = e + (numerator/fact)
        print("The series is === ",e)
    elif i == 1:
        fact = 1
        e = e + (numerator/fact)
        print("The series is === ",e)
    else :
        fact = fact * i
        e = e + (numerator/fact)
        

print("The factorial will be  :",fact)
print("The sum of the series is :",e)

# -------------another way -------------------------------------------


'''
e = (numerator/fact) + (numerator/fact)
# print("The series is === ",e)
for i in range(2,n+1):
    fact = fact * i
    print("The fact === ",fact)
    e = e + (numerator/fact)
    print("The series is === ",e)

print("The sum of the series is :",e)
print("The factorial will be  :",fact)
'''