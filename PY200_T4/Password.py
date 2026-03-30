# Input password
s = input("Enter password: ")

# Check each character
for ch in s:
    if ch.isdigit():
        has_digit = True
    elif ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True

# Check all conditions
if len(s) >= 8 and has_digit and has_upper and has_lower:
    print(" Password is valid (STRONG)")
elif not has_lower:
    print(" Password is not valid (WEAK)")
    print("Password must have 1 lowercase character")
elif not has_upper:
    print("Password is not valid (WEAK)")
    print("Password must have 1 uppercase character")
elif not has_digit:
    print("Password is not valid (WEAK)")
    print("Password must have 1 digit")
else:
    print("\nPassword is WEAK")
    print("Password must be 8 characters long")