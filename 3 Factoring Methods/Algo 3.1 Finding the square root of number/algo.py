m = int(input("Enter a number : "))
e = 0.0001
g2= (m/2)
  #int(input("Enter the first initial guess : "))
g1 = 0
print(g1)
while abs(g1-g2)>e:
    g1 = g2
    g2 = (g1 + (m/g1))/2
    


print("g1 = ",g1)
print("Square root  = ",int(g2))
