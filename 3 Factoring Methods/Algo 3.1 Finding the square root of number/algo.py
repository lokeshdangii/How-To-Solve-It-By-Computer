m = int(input("Enter a number : "))
e = 0.0001
g2= (m/2)
g1 = 0

while abs(g1-g2)>e:
    g1 = g2
    g2 = (g1 + (m/g1))/2
    # print("g1 is = ",g1)
    # print("g2 is = ",g2)    


# print("g1 = ",g1)
print("Square root of {} is : {}".format(m,g2))
