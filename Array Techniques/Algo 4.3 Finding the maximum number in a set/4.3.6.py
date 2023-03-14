arr = [23,31,22,54,75,2,47,9,0,54,27,65,67,33,32,43,45]
x = int(input("Enter a number x to be searched in an array :"))
# check = False
for i in range(0,len(arr)):
    if arr[i] == x:
        print("{} is present at {} index ".format(x,i))
        break
else:
    print("{} not found ".format(x))
    
# if check == True:
#     print("{} is present at {} index ".format(x,i))
# else:
#     print("{} not found ".format(x))