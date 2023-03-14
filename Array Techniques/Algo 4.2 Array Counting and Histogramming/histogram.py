import matplotlib.pyplot as plt

marks = [65, 75, 80, 75, 90, 92, 65, 80, 82, 85, 90, 95, 100, 92, 80, 75]

# Create a histogram with 10 bins
plt.hist(marks, bins=10)

# Add labels and title
plt.xlabel('Marks')
plt.ylabel('Number of Students')
plt.title('Histogram of Examination Marks')

# Display the histogram
plt.show()
