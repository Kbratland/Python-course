import tkinter
from tkinter import *

#TODO convert convo tree to GUI

window = Tk()

def speak():
    global stage
    global entry
    global answer
    global textVar
    answer = entryInput.get()
    if(stage == 1):
        textVar = (f"Hello {answer} how are you?")
    stage +=1
       

stage = 1
entryInput = StringVar()
window.geometry('500x500')
window.title("Talk to me")
textVar = ("Hello, whats your name?")
label = Label(window, textvariable=textVar).pack()
entry = Entry(window, textvariable=entryInput).pack()
button = Button(window,text="Enter", command=speak).pack()


window.mainloop()