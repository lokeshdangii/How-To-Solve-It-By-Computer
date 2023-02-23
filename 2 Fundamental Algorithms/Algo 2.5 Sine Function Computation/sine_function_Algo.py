x = float(input("Enter x :"))
n = int(input("Enter no. of terms : "))
sign = -1
# acc_error = 1*10e-6
term = x
sum = x
for i in range(1,n+1,2):
    term = (term *x*x)/(i*(i+1))
    sum = sum + term 
    sign = -1 * sign
    # if term > acc_error:
    #     break

print("Sine series sum :",sum) 
