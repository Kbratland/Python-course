import tkinter
from tkinter import *


def addTo():
    global listbox
    print("added")
    listbox.insert(END,entry.get())
    entry.delete(0,END)

def deleteFrom():
    print("removed")
    listbox.delete(listbox.curselection)

root = Tk()
# root.geometry("500x500")
# root.resizable(False, False)
root.title("HelloTkinter")
root.configure(background='light blue')

label = Label(root, text ="ToDo List",bg="white").pack()

entry = Entry(root,bg="white").pack()

button = Button(root, text="add", command=addTo,bg="white").pack()
button = Button(root, text="remove", command=deleteFrom,bg="white").pack()

# listvar = StringVar()
#, listvariable=listvar
listbox = Listbox(root).pack()


root.mainloop()