from tkinter import *

root = Tk()
root.title("Converter - (can display up to 16 digit inputs)")
root.geometry("425x250")

my_text = "Test Complete"
tempInput = StringVar()
weightInput = StringVar()
def farenConvert():
    global my_text
    proceed = True
    try:
        originTemp = float(tempInput.get())
        changeTemp = float(tempInput.get())
    except:
        my_text = "Thats not a number, Enter again"
        proceed = False
    if(proceed == True):
        changeTemp = (changeTemp * (9/5)) + 32
        changeTemp = round(changeTemp,2)
        my_text = str(originTemp) + " degrees C is " + str(changeTemp) + " degrees in F"
        templabel.config(text = my_text)
    else:
        my_text = "Thats not a number, Enter again"
        templabel.config(text = my_text)
def celConvert():
    global my_text
    proceed = True
    try:
        originTemp = float(tempInput.get())
        changeTemp = float(tempInput.get())
    except:
        my_text = "Thats not a number, Enter again"
        proceed = False
    if(proceed == True):
        changeTemp = (changeTemp -32) * (5/9)
        changeTemp = round(changeTemp,2)
        my_text = str(originTemp) + " degrees F is " + str(changeTemp) + " degrees in C"
        templabel.config(text = my_text)
    else:
        my_text = "Thats not a number, Enter again"
        templabel.config(text = my_text)
def poundConvert():
    global my_text
    proceed = True
    try:
        originWeight = float(weightInput.get())
        changeWeight = float(weightInput.get())
    except:
        my_text = "Thats not a number, Enter again"
        proceed = False
    if(proceed == True):
        changeWeight = (changeWeight *  2.2046)
        changeWeight = round(changeWeight,2)
        my_text = str(originWeight) + " Kilograms is " + str(changeWeight) + " Pounds"
        weightLabel.config(text = my_text)
    else:
        my_text = "Thats not a number, Enter again"
        weightLabel.config(text = my_text)
def kiloConvert():
    global my_text
    proceed = True
    try:
        originWeight = float(weightInput.get())
        changeWeight = float(weightInput.get())
    except:
        my_text = "Thats not a number, Enter again"
        proceed = False
    if(proceed == True):
        changeWeight = (changeWeight * 0.4535923)
        changeWeight = round(changeWeight,2)
        my_text = str(originWeight) + " Pounds is " + str(changeWeight) + " Kilograms"
        weightLabel.config(text = my_text)
    else:
        my_text = "Thats not a number, Enter again"
        weightLabel.config(text = my_text)

def clearInputs():
    global my_text
    my_text = "Enter a number"
    weightLabel.config(text = my_text)
    templabel.config(text = my_text)
    tempEntry.delete(0,END)
    weightEntry.delete(0,END)

templabel = Label(root,text = "Enter a number")
tempEntry = Entry(root,textvariable=tempInput)
farenButton = Button(root,text = "convert to F",command = farenConvert)
celButton = Button(root,text = "convert to C",command = celConvert)

weightLabel = Label(root,text = "Enter a weight")
weightEntry = Entry(root,textvariable=weightInput)
poundButton = Button(root,text = "convert to Lbs",command = poundConvert)
kiloButton = Button(root,text = "convert to Kg",command = kiloConvert)
clearButton = Button(root,text = "Clear Boxes",command = clearInputs)
 
templabel.pack()
tempEntry.pack()
farenButton.pack()
celButton.pack()
weightLabel.pack()
weightEntry.pack()
poundButton.pack()
kiloButton.pack()
clearButton.pack()
 
root.mainloop()