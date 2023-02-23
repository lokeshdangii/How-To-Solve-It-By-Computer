x = float(input("Enter x :"))
n = int(input("Enter no. of terms : "))

acc_error = 1*10e-6
sum = x
term = x
x2 = x*x
for i in range(3,n+1,2): 
    term = (-term *x2)/(i*(i-1))
    sum = sum + term
    if term > acc_error:
        break

print("Sin series sum :",sum) 

