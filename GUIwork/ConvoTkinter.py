import tkinter as tk
  
root=tk.Tk()

name_var=tk.StringVar()

def submit():
    name=name_var.get()
    name_label.config(text=f"hello {name}")
    print("answer is : " + name)
    name_var.set("")
    

name_label = tk.Label(root, text = 'Hello how are you', font=('calibre',10, 'bold'))
  

name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'),bg="black")
  

sub_btn=tk.Button(root,text = 'Submit', command = submit)
  

name_label.grid(row=0,column=0)
name_entry.grid(row=1,column=0)
sub_btn.grid(row=2,column=0)
  
root.mainloop()