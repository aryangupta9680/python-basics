import tkinter as tk

root = tk.Tk()
root.geometry("300x200")  # Width x Height
canvas = tk.Canvas(root, width=200, height=100, bg='lightblue')
canvas.pack()

# Draw a rectangle
canvas.create_rectangle(50, 20, 150, 80, fill='green')

root.mainloop()

