import math

def sqroot(m):
    e = 0.0001
    g2= (m/2)
    g1 = 0

    while abs(g1-g2)>e:
        g1 = g2
        g2 = (g1 + (m/g1))/2

    # print("Square root of {} is : {}".format(m,g2))
    return g2

def smallest_divisor(num):
    if num%2 == 0:
        return 2
    else:
        r = sqroot(num)
        d = 3
        while num%d ==0 or d>=r:
            d = d+2
            if num%d == 0:
                return d
            else:
                return 1

num = int(input("Enter a number : "))
small_divisor = smallest_divisor(num)
print("Smallest divisor of {} is {}".format(num,small_divisor))

a = 36
sr = math.sqrt(a)
print("Square root is : ",sr)