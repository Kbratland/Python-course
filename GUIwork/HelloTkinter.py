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
# root.configure(background = "dark grey")

label = Label(root, text ="ToDo List").pack()

entry = Entry(root,bg="grey").pack()

button = Button(root, text="add", command=addTo).pack()
button = Button(root, text="remove", command=deleteFrom).pack()

# listvar = StringVar()
#, listvariable=listvar
listbox = Listbox(root).pack()


root.mainloop()