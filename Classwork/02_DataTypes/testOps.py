# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x350")

# Create a Listbox widget
lb = Listbox(win, width=100, height=10, background="purple3", foreground="white", font=('Times 13'), selectbackground="white")

lb.pack()

# Select the list item and delete the item first
# Once the list item is deleted,
# we can insert a new item in the listbox
def edit_current():
   for item in lb.curselection():
      lb.delete(item)
      lb.insert("end", "foo")

# Add items in the Listbox
lb.insert("end", "item1", "item2", "item3", "item4", "item5")

# Add a Button To Edit and Delete the Listbox Item
ttk.Button(win, text="Edit", command=edit_current).pack()