import matplotlib.pyplot as plt

n = [60,50,70,90,80,90,90,80,80,70,60,40]
arr = [0]*101

# print(arr)

for i in n:
    for j in range(0,101):
        if i == j:
            arr[j] = arr[j] +1
        
for k in range(0,101):
    if  arr[k]== 0:
        pass
    else:
        print("Mark count of student for mark {} is {}".format(k,arr[k]) )
    
# print("Marks Count = ",arr)

# Create a histogram with 10 bins
plt.hist(n, bins=10)

# Add labels and title
plt.xlabel('Mark Count')
plt.ylabel('Number of Students')
plt.title('Histogram of Examination Marks')

# Display the histogram
plt.show()




