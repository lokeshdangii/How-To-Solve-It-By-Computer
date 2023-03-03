def random(n):

    m = int(input("Enter the modulus m : "))
    a = int(input("Enter the multiplier a : "))
    b = int(input("Enter the increment b : "))
    x = int(input("Enter the x : "))

    random_num = []
    for i in range(0,n):
        x = (a*x + b)%m
        # print(x)
        random_num.append(x)

    return random_num


n = int(input("enter how many numbers to generate : "))
randomnum = random(n)
print("The random numbers are : ",randomnum) 