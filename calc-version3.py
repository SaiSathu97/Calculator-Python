import tkinter as tk
from tkinter import messagebox
import re

def press(button_text):
    """Handle button press and update the entry field."""
    current_text = entry_field.get()

    # Check for invalid consecutive operators using a regular expression
    if re.search(r'[+\-*/]{2,}', current_text):
        messagebox.showerror("Error", "Invalid Expression! More than one operator in a row.")
        entry_field.delete(0, tk.END)  # Clear the entry field after error
        return
    
    if button_text == "AC":  # Clear the entry field and reset everything
        entry_field.delete(0, tk.END)
    elif button_text == "=":  # Evaluate the expression
        try:
            result = eval(current_text)
            entry_field.delete(0, tk.END)
            entry_field.insert(0, str(result))
        except Exception:
            messagebox.showerror("Error", "Invalid Expression!")
    else:
        entry_field.insert(tk.END, button_text)  # Add the button text to the entry field

def create_button(parent, text, row, col):
    """Helper function to create buttons dynamically."""
    return tk.Button(parent, text=text, font=("Arial", 18), command=lambda: press(text), height=2, width=4)

# Create the main window
root = tk.Tk()
root.title("Pressable Calculator")
root.geometry("400x500")  # Resize window to fit buttons well
root.resizable(True, True)

# Entry field
entry_field = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10, sticky="nsew")

# Configure grid weights to make it resizable
root.grid_rowconfigure(0, weight=1)
for i in range(1, 5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Button layout with "AC" for clear functionality
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "AC", "0", "=", "+"
]

# Create buttons dynamically using a helper function
row_val, col_val = 1, 0
for button in buttons:
    button_widget = create_button(root, button, row_val, col_val)
    button_widget.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the application
root.mainloop()
