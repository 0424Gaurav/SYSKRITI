'''This program finds the mode of a list of numbers without using built-in functions.'''

# mode of statistics program
data = [10, 2, 7, 2, 9, 3, 2]

# Step 1: Create empty lists to store unique values and their counts
unique = []
freq = []

# Step 2: Count the frequency of each unique value
for i in data:
    if i in unique:
        index = unique.index(i)
        freq[index] += 1
    else:
        unique.append(i)
        freq.append(1)
# Step 3: Find the maximum frequency
max_count = freq[0]
mode = unique[0]

for i in range(len(freq)):
    if freq[i] > max_count:
        max_count = freq[i]
        mode = unique[i]

print("Mode:", mode)     #the output - 2, which appears most frequently in the list (3 times)