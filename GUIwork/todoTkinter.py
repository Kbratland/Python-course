from tkinter import *

root=Tk()
root.title("TODO List")
num = 0
# root.geometry(f"350x1100")

name_var=StringVar()

def submit():
    global listbox
    global num
    name=name_var.get()
    name_var.set("")
    if(name != ""):
        listbox.insert(num, name)
        num += 1
        

def delete():
    global num
    listbox.delete(ANCHOR)
    num -=1

name_label = Label(root, text = ' Add to Todo List', font=('calibre',20, 'bold'))

name_entry = Entry(root,textvariable = name_var, font=('calibre',12,'normal'),bg="black")

sub_btn=Button(root,text = 'Enter', command = submit)

sub_btn2=Button(root,text = 'Remove', command = delete)

listbox = Listbox(root,bg="black",height=num,width=40)

name_label.grid(row=0,column=0)
name_entry.grid(row=1,column=0)
sub_btn.grid(row=2,column=0)
sub_btn2.grid(row=3,column=0)
listbox.grid(row=4,column=0)

root.mainloop()