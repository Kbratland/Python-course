from tkinter import *
from tkinter.ttk import *
  
root = Tk()
root.title = ("HelloTkinter")
root.geometry =("300x300")
a = Label(root, text ="Hello World").pack()
b = Label(root, text = "buds to small").pack()
button = Button(root, text = 'press me pls')
button.pack(side = TOP, pady = 0)
  
root.mainloop()