import tkinter as tk
  
root=tk.Tk()
root.title("TODO List")

name_var=tk.StringVar()
num = 0
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
    listbox.delete(tk.ANCHOR)
    num -=1

name_label = tk.Label(root, text = ' Add to Todo List', font=('calibre',10, 'bold'))

name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'),bg="black")

sub_btn=tk.Button(root,text = 'Enter', command = submit)
sub_btn2=tk.Button(root,text = 'Remove', command = delete)
  
listbox = tk.Listbox(root,bg="black",height=num,wrap=WORD)

name_label.grid(row=0,column=0)
name_entry.grid(row=1,column=0)
sub_btn.grid(row=2,column=0)
sub_btn2.grid(row=3,column=0)
listbox.grid(row=4,column=0)
  
root.mainloop()