import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.geometry("200x300")

def accept(event):
    a = entryIntr.get()
    labelWr = tkinter.Label(root, text= a)
    labelWr.grid(column = 0, row = 7, sticky = tkinter.W,padx=5, pady= 5)

listFruit = ['apple','strewberry','orange','pineapple','grapes']
lista_items = tkinter.StringVar(value = listFruit)
listbox = tkinter.Listbox(root,height = 10,width=20, listvariable=lista_items)
listbox.grid(column = 0, row = 0, sticky = tkinter.W)

labelIntr = tkinter.Label(root, text= "Write here: ")
labelIntr.grid(column = 0, row = 5, sticky = tkinter.W)
entryIntr = tkinter.Entry(root)
entryIntr.grid(column = 1, row = 5, sticky = tkinter.E,padx=5, pady= 5)

buttonT = tkinter.Button(root, text="Accept", )
buttonT.bind('<Button-1>', accept)
buttonT.grid(column = 0, row = 6, sticky = tkinter.W,padx=5, pady= 5)

root.mainloop()