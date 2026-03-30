'''Write a Python program to check if the number is positive, negative or zero.
'''

# Input from user
num = float(input("Enter a number: "))

# Check condition
if num > 0:
    print(f"Your entered number {num} is positive.")
elif num < 0:
    print(f"Your entered number {num} is negative.")
else:
    print(f"Your entered number {num} is zero.")