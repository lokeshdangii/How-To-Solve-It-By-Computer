def sqroot(m):
    e = 0.0001
    g2= (m/2)
    g1 = 0

    while abs(g1-g2)>e:
        g1 = g2
        g2 = (g1 + (m/g1))/2

    # print("Square root of {} is : {}".format(m,g2))
    return g2

m = int(input("Enter a number : "))
print("Square root of {} is : {}".format(m,sqroot(m)))