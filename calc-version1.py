# Simple Calculator in Python (Whole Numbers Only)

def get_whole_number(prompt):
    while True:
        try:
            return int(input(prompt))  # Try to get an integer
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get user input for operation
    operation = input("Enter the number of the operation (1/2/3/4): ")

    # Check if the operation is valid
    if operation in ['1', '2', '3', '4']:
        # Get user input for numbers (whole numbers only)
        num1 = get_whole_number("Enter the first number (whole number only): ")
        num2 = get_whole_number("Enter the second number (whole number only): ")

        # Perform the selected operation
        if operation == '1':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is {result}")
        elif operation == '2':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is {result}")
        elif operation == '3':
            result = num1 * num2
            print(f"The result of {num1} * {num2} is {result}")
        elif operation == '4':
            # Check for division by zero
            if num2 != 0:
                result = num1 // num2  # Integer division
                print(f"The result of {num1} / {num2} is {result}")
            else:
                print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please try again.")

# Run the calculator
calculator()
