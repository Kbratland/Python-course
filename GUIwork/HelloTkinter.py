import tkinter  as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
  
root = tk.Tk()
addto = tk.StringVar()
root.geometry("500x500")
root.resizable(False, False)
root.title = ("HelloTkinter")
a = Label(root, text ="ToDo List").pack()
listentry = ttk.Entry(root,textvariable=addto).pack()
button = Button(root, text = 'Enter')
button.pack(side = TOP, pady = 0)
button = Button(root, text = 'remove')
button.pack(side = TOP, pady = 0)
tasks = ('test', 'test2')
taskcount = 1
print(taskcount, "items in list")
# var = tk.Variable(value=tasks)
Listbox = tk.Listbox(root, listvariable = tasks, height = taskcount, selectmode=tk.EXTENDED).pack()
  
root.mainloop()