"""This program finds the mean of a list of number without using built-in functions."""

# mean of statistics program
data = [4, 2, 7, 2, 9, 3, 2]

total = 0     #total is the sum of all the elements 
count = 1    #count is the number of elements in the list
for i in data:
    total = total + i
    count = count + 1

mean = total / count        #Formula for mean = sum all elements / count of total elements

print(f"Mean: {mean}\n")     #the output - 3.625