try:
    a=float(input("Enter your first number: "))
    b=float(input("Enter your second number: "))
    print(f"Sum: {a + b}")
    
    print(f"Product: {a * b}")

    if b != 0:
        print(f"Division: {a/b:.2f}")
    else:
         print("Error: Division by zero is not allowed.")
except ValueError:
    print("Invalid input.Please enter numeric values.")
