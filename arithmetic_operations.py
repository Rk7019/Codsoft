def perform_operation():
    """Gets input, performs calculation, and prints the result."""

    # --- Get Number 1 ---
    while True:
        try:
            num1_str = input("Enter number 1: ")
            num1 = float(num1_str)
            break # Exit loop if conversion is successful
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # --- Get Number 2 ---
    while True:
        try:
            num2_str = input("Enter number 2: ")
            num2 = float(num2_str)
            break # Exit loop if conversion is successful
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # --- Get Operation ---
    valid_operations = ['add', 'subtract', 'multiply', 'divide']
    while True:
        operation = input(f"Enter operation ({', '.join(valid_operations)}): ").lower().strip()
        if operation in valid_operations:
            break
        else:
            print(f"Invalid operation. Please choose from: {', '.join(valid_operations)}")

    # --- Perform Calculation ---
    result = None
    error = None

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            error = "Error: Division by zero"
        else:
            result = num1 / num2

    # --- Display Result ---
    print("-" * 20) # Separator
    if error:
        print(error)
    elif result is not None:
        print(f"Result: {result}")
    else:
        # Should not happen with current logic, but good practice
        print("An unexpected issue occurred.")
    print("-" * 20)

# --- Main Loop ---
print("calculator with basic arithmetic operations.")
print("-----------------------------")

while True:
    perform_operation()
    
    # Ask if the user wants to continue
    again = input("Perform another calculation? (yes/no): ").lower().strip()
    if again != 'yes':
        break

print("\nCalculator finished.")