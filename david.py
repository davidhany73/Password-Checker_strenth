import tkinter as tk
from tkinter import ttk, messagebox
import ast

def detect_endless_loop(code):
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.While):
            if isinstance(node.test, ast.Constant) and node.test.value == True:
                return f"An endless loop detected on line {node.lineno}"
    return "No endless loop detected"

def detect_unsafe_modules(code):
    unsafe_modules = ["pickle", "os"]  # Add more if needed
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
            for alias in node.names:
                if alias.name in unsafe_modules:
                    return f"Unsafe module detected on line {node.lineno}: import {alias.name}"
    return "No unsafe module detected"

def check_password_strength(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long"
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter"
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter"
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit"
    if not any(char in "!@#$%^&*()-_=+`~[{]};:'\",<.>/?\\|" for char in password):
        return "Password must contain at least one special character"
    return "Password strength: Strong"

def check_code():
    code = code_text.get("1.0", "end-1c")
    result = detect_endless_loop(code) + "\n"
    result += detect_unsafe_modules(code)
    messagebox.showinfo("Code Check Result", result)

def check_password():
    password = password_entry.get()
    result = check_password_strength(password)
    messagebox.showinfo("Password Strength", result)

root = tk.Tk()
root.title("Code and Password Checker")
root.geometry("400x300")  # Change the size of the window

# Use ttk style for a more modern look
style = ttk.Style()
style.configure("TFrame", relief="raised", borderwidth=2)  # Use 'raised' relief for 3D appearance
style.configure("TButton", relief="flat", background="#4682B4", foreground="white")  # Styling for buttons

main_frame = ttk.Frame(root, padding=(20, 10))
main_frame.pack(fill=tk.BOTH, expand=True)

code_label = ttk.Label(main_frame, text="Enter code:")
code_label.grid(row=0, column=0, padx=5, pady=5)

code_text = tk.Text(main_frame, height=10, width=50)
code_text.grid(row=1, column=0, padx=5, pady=5)

code_button = ttk.Button(main_frame, text="Check Code", command=check_code)
code_button.grid(row=2, column=0, padx=5, pady=5)

password_label = ttk.Label(main_frame, text="Enter password:")
password_label.grid(row=3, column=0, padx=5, pady=5)

password_entry = ttk.Entry(main_frame, show="*")
password_entry.grid(row=4, column=0, padx=5, pady=5)

password_button = ttk.Button(main_frame, text="Check Password", command=check_password)
password_button.grid(row=5, column=0, padx=5, pady=5)

root.mainloop()
