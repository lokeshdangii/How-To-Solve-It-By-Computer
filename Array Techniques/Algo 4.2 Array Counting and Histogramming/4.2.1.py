import matplotlib.pyplot as plt
marks = [65, 75, 80, 75, 90, 92, 65, 80, 82, 85, 90, 95, 100, 92, 80, 75]

# Create an empty dictionary to store the count of each unique mark
mark_count = {}

# Loop through the list of marks and update the dictionary
for mark in marks:
    if mark in mark_count:
        mark_count[mark] += 1
    else:
        mark_count[mark] = 1

# Print the count of each unique mark
for mark, count in mark_count.items():
    print(f"{mark}: {count}")

# Create a histogram with 10 bins
plt.hist(marks, bins=15)

# Add labels and title
plt.xlabel('percentile')
plt.ylabel('Number of Students')
plt.title('Histogram of Examination Marks')

# Display the histogram
plt.show()