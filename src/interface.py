import tkinter
from tkinter import ttk
import random
import sys



# label_saludo = tkinter.Label(window, text = "Hola", bg="yellow", fg='blue')
# label_saludo.pack(ipadx=50,ipady=50, expand=True)

# labe2_adios = tkinter.Label(window, text = "Adios", bg = "red", fg='white')
# labe2_adios.pack(ipadx=50,ipady=100,fill='y')

# labe3_saludo = tkinter.Label(window, text = "Hola", bg="yellow", fg='blue')
# labe3_saludo.pack(ipadx=50,ipady=50, expand=True)

# labe4_adios = tkinter.Label(window, text = "Adios", bg = "red", fg='white')
# labe4_adios.pack(ipadx=50,ipady=100,fill='y')

# window.columnconfigure(0,weight=1)
# window.columnconfigure(1,weight=3)

# username_label = ttk.Label(window,text = "Username")
# username_label.grid (column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

# username_entry = ttk.Entry(window)
# username_entry.grid(column = 1, row = 0, sticky=tkinter.E, padx=5,pady=5)

# password_label = ttk.Label(window,text = "Password")
# password_label.grid (column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

# password_entry = ttk.Entry(window, show= "*")
# password_entry.grid(column = 1, row = 1, sticky=tkinter.E, padx=5,pady=5)

# login_button = ttk.Button(window,text = "Login")
# login_button.grid(column=1, row=3,sticky=tkinter.E,padx=5, pady=5)

window = tkinter.Tk()

def saludar(event):
    print('Han hecho click en saludar')
    
def saludarDobleClick(event):
    print('Han hecho DOBLE click en saludar')
    
def salir(event):
    print("Adios")
    window.quit()   

boton = tkinter.Button(window, text= 'Haz click')
boton.pack()
boton.bind('<Button-1>', saludar)
boton.bind('<Double-1>', saludarDobleClick)

botonSalir = tkinter.Button(window, text= 'Salir')
botonSalir.pack()
botonSalir.bind('<Button-1>', salir)
window.mainloop()


# window.columnconfigure(0,weight=1)
# window.columnconfigure(0,weight=3)

# selected = tkinter.StringVar()
# checkbox = ttk.Checkbutton(window, text= 'acepto las ondiciones', variable= selected)
# checkbox.grid(column = 1, row = 1)
# r1 = ttk.Radiobutton(window, text = 'si', value = '1', variable=selected)
# r2 = ttk.Radiobutton(window, text = 'No', value = '2', variable=selected)
# r3 = ttk.Radiobutton(window, text = 'Tal vez', value = '3', variable=selected)

# r1.grid(column = 0, row = 1, padx=5, pady=5)
# r2.grid(column = 1, row = 1, padx=5, pady=5)
# r3.grid(column = 2, row = 1, padx=5, pady=5)

# lista = ['Windows', 'macOS', 'Linux', 'MS DOS', 'AmigaOS', 'Beos', 'OS/2']
# lista_items = tkinter.StringVar(value = lista)
# listbox = tkinter.Listbox(window,height = 100, listvariable=lista_items)
# listbox.grid(column = 0, row = 0, sticky = tkinter.W)

window.mainloop()
sys.exit(0)

# frame = ttk.Frame(window)


# label = ttk.Label(frame, text = 'Hola')
# label.grid(column=0,row=0, sticky=tkinter.W, padx=5, pady=5)

# frame.grid(column=0,row=0, sticky=tkinter.W)

colors = ['blue', 'red', 'yellow','purple', 'green', 'black']

for x in range(0,10):
    color = random.randint(0,len(colors)-1)
    color2 = random.randint(0,len(colors)-1)
    label = tkinter.Label(window, text = "etiqueta!", bg = colors[color], fg = colors[color])
    label.place(x  = random.randint(0,100), y = random.randint(0,100))