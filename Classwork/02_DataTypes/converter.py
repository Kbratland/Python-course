import tkinter as tk
from tkinter import *
import time

root=tk.Tk()
root.title("Converter Program")
root.geometry("400x400")

displayVarTemp = StringVar()
displayVarWeight = StringVar()
tempEnter = 0

tempLabel = tk.Label(root, text=displayVarTemp,font=('calibre',20,'normal')).pack()
tempEntry = tk.Entry(root,textvariable=tempEnter,).pack()

farenButton = tk.Button(root, text="Convert to Fahrenheit",font=('calibre',20,'normal')).pack()
celciusButton = tk.Button(root, text="Convert to Celcius",font=('calibre',20,'normal')).pack()