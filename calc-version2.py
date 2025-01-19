import tkinter as tk
from tkinter import messagebox

def calculate():
    """Perform the selected calculation."""
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed!")
                return
            result = num1 // num2  # Integer division
        else:
            messagebox.showerror("Error", "Invalid operation selected!")
            return

        messagebox.showinfo("Result", f"The result is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid whole numbers!")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Input fields
tk.Label(root, text="Enter the first number:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter the second number:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Operation selection
tk.Label(root, text="Select an operation:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
operation_var = tk.StringVar(value="+")
operations_frame = tk.Frame(root)  # Create a frame for operation buttons
operations_frame.grid(row=2, column=1, pady=5, sticky="w")

# Add operation buttons in a single row
for op in ["+", "-", "*", "/"]:
    tk.Radiobutton(operations_frame, text=op, variable=operation_var, value=op).pack(side="left", padx=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
