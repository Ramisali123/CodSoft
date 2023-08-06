from tkinter import *
import tkinter as tk
from tkinter import messagebox 

# Function to add a new task to the list
def add_task():
    task = entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Alert!", "Please add a task.")

# Function to remove the selected task from the list
def remove_task():
    
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Alert!", "Please select at Least one task.")


global entry,task_listbox
# Create the main application window
app = tk.Tk()
app.title("To-Do List")
app.geometry("1000x600")
app.configure(bg="cyan")


# Create the task listbox
task_listbox = Listbox(app,borderwidth=12,font=("Times",14),width = 40,height=15, fg = "blacK",bg = "white",relief = RAISED)
task_listbox.pack(pady=10)

# Create the task entry
entry = Entry(app, font=("Times", 18),width=20,fg = "black",borderwidth=8,bg = "white",relief = RAISED)
entry.pack(pady=10)

# Custom-styled colorful buttons
button_styles = {
    "add": {"bg": "red", "fg": "white"},
    "remove": {"bg": "green", "fg": "white"}   
}

button_frame = Frame(app,bg="cyan")
button_frame.pack(pady=10)

Create = Button(button_frame, text="Create Task", command=add_task,borderwidth=6,font=("Times",14),width = 8, fg = "white",bg = "green", padx=5,pady=5,relief = RAISED)
Create.grid(row=0, column=0,padx=40)



Delete = Button(button_frame, text="Delete", command=remove_task,borderwidth=6,font=("Times",14),width = 8, fg = "white",bg = "red", padx=5,pady=5,relief = RAISED)
Delete.grid(row=4, column=0,padx=40)



# Start the main event loop
app.mainloop()
