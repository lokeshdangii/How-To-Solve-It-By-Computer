setofmarks = [35,60,55,45,79,37,68]
totalstds = len(setofmarks)
passmarks = 50

passcount = 0
for i in setofmarks:
    if i >= passmarks:
        passcount = passcount+1

print("the number of students passed are : ",passcount)

# percentage pass rate of students
percentage = (passcount/totalstds)*100
print("the percentage pass rate is : ", percentage)
