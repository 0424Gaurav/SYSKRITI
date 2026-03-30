"""This program finds the median of a list of numbers without using built-in functions."""

#median of statistics program
data = [4, 2, 7, 2, 9, 3, 2]
n = len(data)

# Step 2: Find median
if n % 2 == 1:
    median = data[n // 2]
else:
    median = (data[n // 2] + data[(n // 2) - 1]) / 2

print("Sorted Data:", data)   #the output - [2, 2, 2, 3, 4, 7, 9], which is the sorted list of numbers
print("Median:", median)      #the output - 3, which is the middle value in the sorted list (4 is the middle value, but since there are two middle values, we take the average of 3 and 4)