import tkinter
from tkinter import *

# HELP TKINTER ANGRY AT ME

def addTo():
    global listbox
    print("added")
    listbox.insert(END,entry.get())
    entry.delete(0,END)

def deleteFrom():
    print("removed")
    listbox.delete(listbox.curselection)

root = Tk()
root.title("HelloTkinter")

label = Label(root, text ="ToDo List").pack()

entry = Entry(root,bg="grey").pack()

button = Button(root, text="add", command=addTo).pack()
button = Button(root, text="remove", command=deleteFrom).pack()

# listvar = StringVar()
#, listvariable=listvar
listbox = Listbox(root).pack()


root.mainloop()