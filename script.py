import tkinter as tk
from tkinter import messagebox
import hashlib
import re

# Function to test password strength
def test_password_strength(password):
    strength = 0
    if len(password) >= 12:
        strength += 1
    if re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'[a-z]', password):
        strength += 1
    if re.search(r'[0-9]', password):
        strength += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    
    if strength == 5:
        return "Very Strong"
    elif strength >= 3:
        return "Strong"
    else:
        return "Weak"

# Function to check password against common hashes
def check_password_against_common_hashes(password):
    common_hashes = {
        "5f4dcc3b5aa765d61d8327deb882cf99": "password",  # MD5 hash for "password"
        "e99a18c428cb38d5f260853678922e03": "abc123",    # MD5 hash for "abc123"
    }
    password_hash = hashlib.md5(password.encode()).hexdigest()
    if password_hash in common_hashes:
        return f"Weak password: found in hash lists ({common_hashes[password_hash]})"
    return "The password is secure"

# Function to handle the "Test" button click
def check_password():
    password = entry.get()
    strength = test_password_strength(password)
    hash_check = check_password_against_common_hashes(password)
    
    # Show the results in a messagebox
    result_message = f"Password Strength: {strength}\nHash Check: {hash_check}"
    messagebox.showinfo("Test Results", result_message)

# Create the main application window
app = tk.Tk()
app.title("Password Strength Tester")

# Create and place the label
label = tk.Label(app, text="Enter your password:")
label.pack()

# Create and place the password entry field
entry = tk.Entry(app, show="*")
entry.pack()

# Create and place the "Test" button
button = tk.Button(app, text="Test", command=check_password)
button.pack()

# Run the application
app.mainloop()