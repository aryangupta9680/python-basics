import tkinter as tk

def say_hello():
    print("Hello!")

root = tk.Tk()
root.title("My Tkinter Window")
root.geometry("300x200")  # Width x Height
btn = tk.Button(root, text="Click Me", command=say_hello)
btn.pack()

root.mainloop()