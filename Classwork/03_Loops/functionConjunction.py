import time
from tkinter import *

root = Tk()
root.title("Click")
root.geometry("120x200")
count = int(0)


def countCom(addNum):
    global count
    global countLabel

    count += addNum
    tCount = str(count)
    time.sleep(0.5)
    countLabel.config(text=tCount)


countLabel = Label(root, text="Count here")

funcButton = Button(root, text="Count + 1", command=lambda: countCom(1))
funcButton2 = Button(root, text="Count + 5", command=lambda: countCom(5))
funcButton3 = Button(root, text="Count + 10", command=lambda: countCom(10))
funcButtonn1 = Button(root, text="Count - 1", command=lambda: countCom(-1))
funcButtonn2 = Button(root, text="Count - 5", command=lambda: countCom(-5))
funcButtonn3 = Button(root, text="Count - 10", command=lambda: countCom(-10))


countLabel.pack()

funcButton.pack()
funcButton2.pack()
funcButton3.pack()
funcButtonn1.pack()
funcButtonn2.pack()
funcButtonn3.pack()


root.mainloop()
