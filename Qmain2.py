import tkinter as tk

def change_color():
    # Changes the button's background color to yellow when clicked
    button.config(bg="yellow", activebackground="yellow")

# Create the main window
root = tk.Tk()
root.title("Special Midterm Exam in OOP")
root.geometry("400x330")

# Create the button and center it in the window
button = tk.Button(
    root, 
    text="Click to Change Color", 
    command=change_color,
    padx=10,  # Horizontal internal padding
    pady=5    # Vertical internal padding
)
button.pack(expand=True)

# Start the application loop
root.mainloop()
