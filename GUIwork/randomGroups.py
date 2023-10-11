from random import *
from tkinter import *
from shelve import *
from math import *

root = Tk()
root.title("The Student Organizer 2.0")
num = 0

name_var = StringVar()
num_var = IntVar()
ginVar = StringVar()

listbox = Listbox(root, height=num, width=30)
list_2 = Listbox(root, height=num, width=30)


def submit(event):
    print("doing submit")
    global listbox
    global num
    name = name_var.get()
    name_var.set("")
    if (name != ""):
        listbox.insert(num, f"{num + 1}. " + name)
        num += 1


def changeEntry():
    print("doing edit")
    global listbox
    global num
    changeNum = num_var.get() - 1
    name = name_var.get()
    if (name != ""):
        listbox.insert(changeNum, f"{changeNum + 1}. ")
        listbox.delete(changeNum + 1)


def delete():
    print("doing delete")
    global num
    listbox.delete(ANCHOR)
    if num > 0:
        num -= 1


def quitList(listBin, list2):
    print("doing quit")
    global num
    listFile = open("listFile")
    tempList = []
    temp2 = []
    for lp in range(num):
        tempList.append(listBin.get(lp))
        temp2.append(list2.get(lp))
    listFile["groupHold"] = temp2
    listFile["numHold"] = num
    listFile["listHold"] = tempList
    listFile.close()
    exit()


def loadList(listBin, list2):
    print("doing load")
    global num
    try:
        listFile = open("listFile")
        tempList2 = listFile["listHold"]
        tempG = listFile["groupHold"]
        num = listFile["numHold"]
        # print(tempList2)
        for lp in range(len(tempList2)-1):
            listBin.insert(lp, tempList2[lp])
            list2.insert(lp, tempG[lp])
        listFile.close()
    except:
        pass


def randomize(listIn, listOut, amount, mode):
    print("doing randomize")
    global num
    listOut.delete(0, END)
    tempList = []
    for lp in range(num):
        tempList.append(listIn.get(lp))
    if mode == 1:
        for lp in range(len(tempList)):
            listOut.insert(lp, tempList[lp] +
                           f" is in group {randint(1,amount)}")
    else:
        temp2 = []
        holdInt = len(tempList)
        for main in range(amount):
            for lp in range(ceil(holdInt/amount)):
                print(ceil(holdInt/amount))
                try:
                    wordIn = tempList.pop(randint(0, len(tempList)-1))
                except:
                    break
                if wordIn != "":
                    temp2.append(wordIn + f" is in group {main+1}")
                print(tempList)
            main += 1
    if mode != 1:
        for lp in range(0, len(temp2)):
            listOut.insert(lp, temp2[lp])


loadList(listbox, list_2)

root.bind('<Return>', submit)

name_label = Label(root, text=" Add a student's name ",
                   font=('calibre', 20, 'bold'))

name_entry = Entry(root, textvariable=name_var, font=(
    'calibre', 12, 'normal'), bg="black")
num_label = Label(root, text='Edit Name:', font=('calibre', 20, 'bold'))

num_entry = Entry(root, textvariable=num_var, font=(
    'calibre', 12, 'normal'), bg="black")

sub_btn = Button(root, text='Enter', command=lambda: submit(1))

sub_btn2 = Button(root, text='Remove Selected', command=delete)

sub_btn4 = Button(root, text="Group by name", command=lambda: randomize(
    listbox, list_2, int(ginVar.get()), mode=1))
sub_btn5 = Button(root, text="Group by number", command=lambda: randomize(
    listbox, list_2, int(ginVar.get()), mode=2))

sub_btn3 = Button(root, text="Edit", command=changeEntry)

groups_label = Label(root, text="Enter the amount of groups")
groups_entry = Entry(root, textvariable=ginVar, font=(
    'calibre', 12, 'normal'), bg="black")
g2_label = Label(root, text='Groups:', font=('calibre', 15, 'bold'))
n1_label = Label(root, text='Names:', font=('calibre', 15, 'bold'))


exitButton = Button(root, text="Save and quit",
                    command=lambda: quitList(listbox, list_2))

name_label.grid(row=0, column=1)
name_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)
sub_btn2.grid(row=3, column=1)
groups_label.grid(row=4, column=1)
groups_entry.grid(row=5, column=1)
sub_btn4.grid(row=5, column=0)
sub_btn5.grid(row=5, column=2)
num_label.grid(row=6, column=1)
num_entry.grid(row=7, column=1)
sub_btn3.grid(row=8, column=1)
n1_label.grid(row=9, column=1)
listbox.grid(row=10, column=1)
g2_label.grid(row=11, column=1)
list_2.grid(row=12, column=1)
exitButton.grid(row=13, column=1, padx=5, pady=5)

root.mainloop()