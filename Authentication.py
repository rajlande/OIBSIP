import tkinter as tk
from tkinter import messagebox

# Define a dictionary to store user credentials
users = {}

# Function to register a new user
def register():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        users[username] = password
        messagebox.showinfo("Success", "User registered successfully!")
    else:
        messagebox.showerror("Error", "Please enter a username and password.")

# Function to login an existing user
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username in users and users[username] == password:
        messagebox.showinfo("Success", "Login successful!")
        secured_page()
    else:
        messagebox.showerror("Error", "Invalid username or password.")

# Function to access a secured page
def secured_page():
    messagebox.showinfo("Welcome", "Welcome to the secured page!")

# Create a Tkinter window
window = tk.Tk()
window.title("Login Authentication System")

# Create labels and entry widgets for username and password
username_label = tk.Label(window, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(window)
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = tk.Label(window, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Create buttons for register, login, and exit
register_button = tk.Button(window, text="Register", command=register)
register_button.grid(row=2, column=0, padx=10, pady=10)

login_button = tk.Button(window, text="Login", command=login)
login_button.grid(row=2, column=1, padx=10, pady=10)

exit_button = tk.Button(window, text="Exit", command=window.quit)
exit_button.grid(row=2, column=2, padx=10, pady=10)

# Run the Tkinter event loop
window.mainloop()
