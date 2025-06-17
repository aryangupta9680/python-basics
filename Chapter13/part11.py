import tkinter as tk

root = tk.Tk()
root.title("My Tkinter Window")
root.geometry("300x200")  # Width x Height


text = tk.Text(root, height=5, width=30)
text.pack()

root.mainloop()