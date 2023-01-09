import tkinter
from tkinter import ttk


root = tkinter.Tk()

def restart(event):
    selected.set(" ")

selected = tkinter.StringVar()

r1 = ttk.Radiobutton(root, text = 'Option 1', value = '1', variable=selected)
r2 = ttk.Radiobutton(root, text = 'Option 2', value = '2', variable=selected)
r3 = ttk.Radiobutton(root, text = 'Option 3', value = '3', variable=selected)

r1.grid(column = 0, row = 1)
r2.grid(column = 0, row = 2)
r3.grid(column = 0, row = 3)

button1 = tkinter.Button(root, text = 'Restart')
button1.grid(column = 2, row = 4)
button1.bind('<Button-1>', restart)

root.mainloop()