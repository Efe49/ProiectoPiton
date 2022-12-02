from tkinter import filedialog
from tkinter import *
import tkinter as tk
import funcionesInterfaz


colorPrincipal = "#F3E0B0"

root = tk.Tk()
barraMenu = Menu(root)
root.title('Gestor de audiotecas')
root.config(background=colorPrincipal)
root.config(menu=barraMenu)
root.resizable(True, True)
root.geometry('600x300')

filemenu = Menu(barraMenu, tearoff=0)
filemenu.add_command(
    label="Consultar",
    accelerator="Ctrl+O",
    command=lambda: [funcionesInterfaz.show_file(root)]
)
filemenu.add_command(
    label="Nueva",
    accelerator="Ctrl+N",
    command=lambda: [funcionesInterfaz.new_file(root)]
)
filemenu.add_command(
    label="Modificar",
    accelerator="Ctrl+S",
    command=lambda: [funcionesInterfaz.edit_file(root)]
)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)


helpmenu = Menu(barraMenu, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Ete dani es un trolsillo ...")

barraMenu.add_cascade(label="Archivo", menu=filemenu)
barraMenu.add_cascade(label="Ayuda", menu=helpmenu)

a = Label(root, text="Bienvenido a tu gestor de audiotecas",
          font=("Arial", 20), bg=colorPrincipal)
a.pack(pady=20)

root.mainloop()
