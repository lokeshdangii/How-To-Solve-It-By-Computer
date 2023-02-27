def dectobin(num):
    temp= num
    i = 1
    sum = 0
    while temp!=0:
        rem = int(temp%2)
        sum = sum +i*rem
        i= i*10
        temp= temp/2
    print("Binary Number =", sum)
    return sum

num = int(input("Enter any Number "))
dectobin(num)