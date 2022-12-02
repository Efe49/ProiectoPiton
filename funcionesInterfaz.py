from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import xml.etree.ElementTree as ET
from tkinter import *
from random import *


def show_file(root):
    filetypes = (
        ('Audiotecas', '*.xml'),
        ('Cualquier archivo', '*.*')
    )

    filename = fd.askopenfilename(
        title='Selecciona tu audioteca',
        initialdir='/',
        filetypes=filetypes)

    show_window(root, filename)


def new_file(root):
    filename = fd.askdirectory(
        title='Selecciona donde guardar tu audioteca',
        initialdir='/')

    new_file_window(root, filename)


def new_file_window(root, directory):
    newWindow = Toplevel(root)
    newWindow.title(directory)
    newWindow.geometry("600x800")
    barraMenu = Menu(newWindow)
    newWindow.config(menu=barraMenu)
    saveMenu = Menu(barraMenu, tearoff=0)
    addMenu = Menu(barraMenu, tearoff=0)
    audiotecaName = "\Audioteca-"+str(randint(0, 5000))+".xml"
    saveMenu.add_command(label="Guardar", command=lambda: [save_changes(entries, tree, raiz, directory+audiotecaName), newWindow.destroy(), showinfo(
        title='Gestor de Audiotecas',
        message="Audioteca en : \n"+directory+"\n modificada correctamente"
    )])
    addMenu.add_command(label="Añadir Disco", command=lambda: [
        new_disc(raiz, entries, newWindow)])
    barraMenu.add_cascade(label="Guardar", menu=saveMenu)
    barraMenu.add_cascade(label="Añadir disco", menu=addMenu)
    raiz = ET.Element("audioteca")
    tree = ET.ElementTree(raiz)
    entries = []
    new_disc(raiz, entries, newWindow)


def show_window(root, nombreFichero):
    newWindow = Toplevel(root)
    newWindow.title(nombreFichero)
    newWindow.geometry("600x800")
    tree = ET.parse(nombreFichero)
    raiz = tree.getroot()
    for disco in raiz:
        Label(newWindow, text="Disco: ", font=("Arial", "15")).pack()
        for atributo in disco:

            Label(newWindow, text=atributo.tag.upper() + " : " +
                  atributo.text, font=("Arial", "10")).pack()


def edit_file(root):
    filetypes = (
        ('Audiotecas', '*.xml'),
        ('Cualquier archivo', '*.*')
    )

    filename = fd.askopenfilename(
        title='Selecciona tu audioteca',
        initialdir='/',
        filetypes=filetypes)

    edit_window(root, filename)


def edit_window(root, nombreFichero):
    newWindow = Toplevel(root)
    newWindow.title(nombreFichero)
    newWindow.geometry("600x800")
    barraMenu = Menu(newWindow)
    newWindow.config(menu=barraMenu)
    saveMenu = Menu(barraMenu, tearoff=0)
    addMenu = Menu(barraMenu, tearoff=0)
    saveMenu.add_command(label="Guardar", command=lambda: [save_changes(entries, tree, raiz, nombreFichero), newWindow.destroy(), showinfo(
        title='Gestor de Audiotecas',
        message="Audioteca : \n"+nombreFichero+"\n modificada correctamente"
    )])
    addMenu.add_command(label="Añadir Disco", command=lambda: [
        new_disc(raiz, entries, newWindow)])
    barraMenu.add_cascade(label="Guardar", menu=saveMenu)
    barraMenu.add_cascade(label="Añadir disco", menu=addMenu)
    tree = ET.parse(nombreFichero)
    raiz = tree.getroot()
    entries = []
    for disco in raiz:
        title = Label(newWindow, text="Disco: ", font=("Arial", "15"))
        title.pack()
        aux = []
        labels = []
        for atributo in disco:

            label = Label(newWindow, text=atributo.tag.upper() +
                          " : ", font=("Arial", "10"))
            label.pack()
            s = StringVar(newWindow, atributo.text)
            en = Entry(newWindow, textvariable=s)
            en.pack()
            labels.append(label)
            aux.append(en)

        delete = ttk.Button(newWindow, text="Eliminar")
        delete.config(command=lambda disco=disco, delete=delete, y=aux, x=labels, title=title: [
                      delete_disc(entries, y, x), title.destroy(), raiz.remove(disco), delete.pack_forget()])
        delete.pack(pady=10)
        entries.extend(aux)


def delete_disc(entries, aux, labels):
    copia = []
    for entry in entries:
        if entry in aux:
            copia.append(entry)
    for toDel in copia:
        entries.remove(toDel)
    for entry in aux:
        entry.destroy()
    for label in labels:
        label.destroy()


def new_disc(raiz, entries, newWindow):
    newDisc = ET.Element("disco")
    newName = ET.SubElement(newDisc, "nombre")
    newArtist = ET.SubElement(newDisc, "artista")
    newGenre = ET.SubElement(newDisc, "genero")
    raiz.append(newDisc)
    Label(newWindow, text="Disco: ", font=("Arial", "15")).pack()
    for atributo in newDisc:
        label = Label(newWindow, text=atributo.tag.upper() +
                      " : ", font=("Arial", "10"))
        label.pack()
        s = StringVar(newWindow, atributo.text)
        en = Entry(newWindow, textvariable=s)
        en.pack()
        entries.append(en)


def save_changes(entries, tree, raiz, nombreFichero):
    for disco in raiz:
        for atributo in disco:
            atributo.text = entries.pop(0).get()
    with open(nombreFichero, 'wb') as f:
        tree.write(f, encoding='utf-8')
