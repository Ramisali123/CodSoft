import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    password_length = int(length_entry.get())

    if password_length < 6:
        messagebox.showerror("Error", "Password length should be at least 6 characters.")
        return

    complexity_options = {
        "uppercase": string.ascii_uppercase,
        "lowercase": string.ascii_lowercase,
        "digits": string.digits,
        "special": string.punctuation,
        "combine":string.printable
    }

    selected_complexity = [complexity_var.get()]
    characters = "".join(complexity_options[option] for option in selected_complexity)
    
    if not characters:
        messagebox.showerror("Error", "Please select at least one complexity option.")
        return

    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

# Create the main application window
app = tk.Tk()
app.title("Password Generator")
app.geometry("400x500")

# Complexity options
complexity_label = tk.Label(app,background="cyan", text="Select Complexity:")
complexity_label.pack(pady=10)

complexity_var = tk.StringVar()
complexity_var.set("lowercase")
complexity_options = ["uppercase", "lowercase", "digits", "special","combine"]

for option in complexity_options:
    complexity_checkbox = tk.Checkbutton(app, background="cyan",text=option.capitalize(), variable=complexity_var, onvalue=option)
    complexity_checkbox.pack(anchor=tk.W)

# Password length
length_label = tk.Label(app, text="Password Length:")
length_label.pack(pady=5)

length_entry = tk.Entry(app)
length_entry.pack(pady=5)

# Generate button
generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Generated password
password_label = tk.Label(app, text="Generated Password:")
password_label.pack()

password_entry = tk.Entry(app, show="")
password_entry.pack(pady=5)

# Start the main event loop
app.mainloop()
