# Cosine function algorithm

x = float(input("Enter x :"))
n = int(input("Enter no. of terms : "))

acc_error = 1*10e-6
sum = 1
term = 1
x2 = x*x
for i in range(2,n+1,2): 
    term = (-term *x2)/(i*(i-1))
    sum = sum + term
    if term > acc_error:
        break

print("Cos series sum :",sum) 

# 0.99500417