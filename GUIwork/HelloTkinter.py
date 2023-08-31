import tkinter
from tkinter import *


def addTo():
    print("added")
    listvar.insert(END,entry.get())
    entry.delete(0,END)

def deleteFrom():
    print("removed")
    listbox.delete(listbox.curselection)

root = Tk()
root.geometry("500x500")
root.resizable(False, False)
root.title("HelloTkinter")

label = Label(root, text ="ToDo List").pack()

entry = Entry(root).pack()

button = Button(root, text="add", command=addTo).pack()
button = Button(root, text="remove", command=deleteFrom).pack()

listvar = StringVar()

listbox = Listbox(root, bg="light blue", listvariable=listvar).pack()


root.mainloop()