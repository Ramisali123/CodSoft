from tkinter import *
import tkinter as tk


def on_button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create the main application window
app = tk.Tk()
app.title("Calculator")
app.geometry("1000x600")

# Center the frame on the window
frame = tk.Frame(app,background="cyan", width=1000, height=600)
frame.pack_propagate(False)  # Prevent the frame from resizing to its contents
frame.pack()

# Create the entry field for displaying calculations
entry = tk.Entry(frame,background="red", font=("Arial", 30), justify="right")
entry.pack(pady=20, padx=10, fill=tk.X)

# Custom button styles
button_styles = {
    "bg": "red",  # Background color
    "fg": "white",    # Foreground (text) color
    "activebackground": "red",
    "activeforeground": "white",
    "borderwidth": 8,
    "relief": tk.GROOVE,
    "font": ("Arial", 30),
    "padx": 30,
    "pady": 5,
}

# Create the buttons
button_values = [
    ("7","8","9","/"),
    ("4","5","6","*"),
    ("1","2","3","-"),
    ("C", "0", "=", "+"),
]

for i, row_values in enumerate(button_values):
    button_row = tk.Frame(frame)
    button_row.pack()

    for value in row_values:
        button = tk.Button(button_row, text=value, **button_styles)
        button.pack(side=tk.LEFT, padx=10, pady=10)
        button.bind("<Button-1>", on_button_click)

# Center the frame on the window
app.update()
frame.place(x=(app.winfo_width() - frame.winfo_width()) // 2, y=(app.winfo_height() - frame.winfo_height()) // 2)

# Start the main event loop
app.mainloop()
