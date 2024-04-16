import tkinter as tk
from tkinter import messagebox

def assess_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    strength = 0
    feedback = ""

    if length >= 8:
        strength += 1
    if has_upper:
        strength += 1
    if has_lower:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    if strength == 5:
        feedback = "Strong"
    elif strength >= 3:
        feedback = "Moderate"
    else:
        feedback = "Weak"

    return feedback

def check_password_strength():
    password = entry_password.get()
    strength = assess_password_strength(password)
    messagebox.showinfo("Password Strength", f"Password strength: {strength}")

# Create main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create password label and entry
label_password = tk.Label(root, text="Enter Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Create check button
button_check = tk.Button(root, text="Check Strength", command=check_password_strength)
button_check.pack(pady=5)

root.mainloop()
