binary_num = int(input("Enter a binary number : ")) # 11001
rem = 1
decimal = 0
two_pow = 1

while binary_num != 0:
    rem = int(binary_num%10)
    binary_num = int(binary_num/10)
    

    if rem == 1:
        decimal = decimal + two_pow  
    else:
        decimal = decimal + 0
    two_pow = two_pow * 2

print("Decimal no is : ",decimal)
