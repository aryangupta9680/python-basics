import tkinter as tk

root = tk.Tk()  # Create the main window
root.title("My Tkinter Window")
root.geometry("300x200")  # Width x Height


entry = tk.Entry(root)
entry.pack()

root.mainloop()