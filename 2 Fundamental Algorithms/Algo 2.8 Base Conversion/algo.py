dec_num = int(input("Enter a decimal number :"))
oct_num = 0
q = dec_num

while q == 0:
    rem = dec_num%8
    print("Remainder is :",rem)
    oct_num = oct_num * 10 + rem
    print("octal = ",oct_num)
    q = int(dec_num/8)


print("octal = ",oct_num)
print("the octal conversion of {} is {}".format(dec_num,oct_num))