n = int(input("Enter a number : "))
reverse = 0

while n > 0:
    rem = n%10
    # print("Teh remainder is : ",rem)
    reverse = reverse * 10 + rem
    # print("the reverse is : ",reverse)
    n = int(n/10)
    # print("the number is : ",n)
    
print("The reverse of a number will be => ",reverse)


