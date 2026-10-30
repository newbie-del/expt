%load_ext rpy2.ipython

%pip install rpy2

# Conditional Branching

# Input three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Find the largest number
if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

# Check positive, negative or zero
if a > 0:
    print("First number is positive")
elif a < 0:
    print("First number is negative")
else:
    print("First number is zero")

# Check even or odd
if a % 2 == 0:
    print("First number is even")
else:
    print("First number is odd")

# Arithmetic operations
choice = int(input(
    "Enter 1 for Addition, 2 for Subtraction, 3 for Multiplication: "
))

if choice == 1:
    result = a + b
elif choice == 2:
    result = a - b
elif choice == 3:
    result = a * b
else:
    result = "Invalid choice"

print("Result:", result)