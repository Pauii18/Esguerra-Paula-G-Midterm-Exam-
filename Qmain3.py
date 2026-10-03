import tkinter as tk

def display_fullname():
    fullname = entry_input.get()
    
    entry_output.delete(0, tk.END)
    
    entry_output.insert(0, fullname)

root = tk.Tk()
root.title("Midterm in OOP")
root.geometry("480x250")

main_frame = tk.Frame(root, padx=30, pady=40)
main_frame.pack(expand=True, fill="both")

label_prompt = tk.Label(
    main_frame, 
    text="Enter your fullname:", 
    fg="red", 
    font=("Times New Roman", 11)
)
label_prompt.grid(row=0, column=0, sticky="w", padx=10, pady=10)

entry_input = tk.Entry(main_frame, font=("Times New Roman", 11), width=18)
entry_input.grid(row=0, column=1, padx=10, pady=10)


button_display = tk.Button(
    main_frame, 
    text="Click to display your Fullname", 
    fg="red", 
    font=("Times New Roman", 11),
    command=display_fullname
)
button_display.grid(row=1, column=0, sticky="w", padx=10, pady=10)

entry_output = tk.Entry(main_frame, font=("Times New Roman", 11), width=18)
entry_output.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
