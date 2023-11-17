from tkinter import *
root = Tk()

text = "new text"


def changeText():
    global text
    label.config(text=text)


button = Button(root, text="change text", command=changeText)

label = Label(root, text="old text")

label.pack()
button.pack()

root.mainloop()
