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










# Program to demonstrate Conditional Branching in R

# Accept input from the user
cat("CONDITIONAL BRANCHING IN R\n")
cat("--------------------------\n")

num = as.numeric(readline("Enter a number: "))

# 1. Simple if statement
cat("\n1. Simple IF Statement\n")

if (num > 0) {
  cat("The number is positive.\n")
}

# 2. if-else statement
cat("\n2. IF-ELSE Statement\n")

if (num %% 2 == 0) {
  cat("The number is even.\n")
} else {
  cat("The number is odd.\n")
}

# 3. if-else-if ladder
cat("\n3. IF-ELSE-IF Ladder\n")

if (num > 0) {
  cat("Number is positive.\n")
} else if (num < 0) {
  cat("Number is negative.\n")
} else {
  cat("Number is zero.\n")
}

# 4. Nested if statement
cat("\n4. Nested IF Statement\n")

if (num >= 0) {
  if (num == 0) {
    cat("The number is zero.\n")
  } else {
    cat("The number is positive.\n")
  }
} else {
  cat("The number is negative.\n")
}

# 5. Grade calculation using conditional branching
cat("\n5. Grade Calculation\n")

marks = as.numeric(readline("Enter marks (0-100): "))

if (marks < 0 || marks > 100) {
  cat("Invalid marks! Enter marks between 0 and 100.\n")
} else if (marks >= 90) {
  cat("Grade: A+\n")
} else if (marks >= 80) {
  cat("Grade: A\n")
} else if (marks >= 70) {
  cat("Grade: B\n")
} else if (marks >= 60) {
  cat("Grade: C\n")
} else if (marks >= 40) {
  cat("Grade: D\n")
} else {
  cat("Grade: F (Fail)\n")
}

cat("\nProgram executed successfully!\n")

