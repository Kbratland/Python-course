from random import *
from tkinter import *
from shelve import *

root = Tk()
root.title("The Student Organizer 2.0")
num = 0

name_var = StringVar()
num_var = IntVar()
ginVar = StringVar()

listbox = Listbox(root, height=num, width=40)
list_2 = Listbox(root, height=num, width=40)


def submit(event):
    global listbox
    global num
    name = name_var.get()
    name_var.set("")
    if (name != ""):
        listbox.insert(num, f"{num + 1}. " + name)
        num += 1


def changeEntry():
    global listbox
    global num
    changeNum = num_var.get() - 1
    name = name_var.get()
    if (name != ""):
        listbox.insert(changeNum, f"{changeNum + 1}. ")
        listbox.delete(changeNum + 1)


def delete():
    global num
    listbox.delete(ANCHOR)
    if num > 0:
        num -= 1


def quitList(listBin, list2):
    global num
    listFile = open("listFile")
    tempList = []
    temp2 = []
    for lp in range(num):
        tempList.append(listBin.get(lp))
        temp2.append(list2.get(lp))
    # print(tempList)
    listFile["groupHold"] = temp2
    listFile["numHold"] = num
    listFile["listHold"] = tempList
    listFile.close()
    exit()


def loadList(listBin, list2):
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


def randomize(listIn, listOut, amount):
    global num
    listOut.delete(0, END)
    # print("starting randomize")
    tempList = []
    for lp in range(num):
        tempList.append(listIn.get(lp))
    for lp in range(len(tempList)):
        listOut.insert(lp, tempList[lp] + f" is in group {randint(1,amount)}")
    # print(tempList)


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

sub_btn4 = Button(root, text="Group students", command=lambda: randomize(
    listbox, list_2, int(ginVar.get())))

sub_btn3 = Button(root, text="Edit", command=changeEntry)

groups_label = Label(root, text="Enter the amount of groups")
groups_entry = Entry(root, textvariable=ginVar, font=(
    'calibre', 12, 'normal'), bg="black")
g2_label = Label(root, text='Groups:', font=('calibre', 15, 'bold'))
n1_label = Label(root, text='Names:', font=('calibre', 15, 'bold'))


exitButton = Button(root, text="Save and quit",
                    command=lambda: quitList(listbox, list_2))

name_label.grid(row=0, column=0)
name_entry.grid(row=1, column=0)
sub_btn.grid(row=2, column=0)
sub_btn2.grid(row=3, column=0)
groups_label.grid(row=4, column=0)
groups_entry.grid(row=5, column=0)
sub_btn4.grid(row=6, column=0)
num_label.grid(row=7, column=0)
num_entry.grid(row=8, column=0)
sub_btn3.grid(row=9, column=0)
n1_label.grid(row=10, column=0)
listbox.grid(row=11, column=0)
g2_label.grid(row=12, column=0)
list_2.grid(row=13, column=0)
exitButton.grid(row=14, column=0, padx=10, pady=10)

root.mainloop()
