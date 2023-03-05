x = int(input("Enter a number x : "))
n = int(input("Enter a power n : "))
p = 1

for i in range(1,n+1):
    p = p*x
    # print("value = ",p)

print("value after evaluation : ",p)