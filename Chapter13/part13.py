import tkinter as tk

root = tk.Tk()
root.geometry("300x200")  # Width x Height
frame = tk.Frame(root, borderwidth=2, relief="sunken")
frame.pack(padx=10, pady=10)

btn1 = tk.Button(frame, text="Button 1")
btn2 = tk.Button(frame, text="Button 2")
btn1.pack(side="left")
btn2.pack(side="left")

root.mainloop()