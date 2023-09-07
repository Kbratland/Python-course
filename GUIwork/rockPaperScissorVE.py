import random
import tkinter as tk
from tkinter import *
import time

root=tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")

score = 0
enScore = 0

def rockPlayer():
    print("rock")
    global score
    global enScore
    global displayVar
    enChoice = random.randrange(1,4)
    print(enChoice)
    displayVar = "thinking"
    time.sleep(.15)
    if(enChoice ==3 ):
        displayVar = "You chose rock, I chose paper, I win"
        enScore += 1
    elif(enChoice == 2):
        displayVar = "You chose rock, I chose scissors, You win"
        score += 1
    elif(enChoice == 1):
        displayVar = "You chose rock, I chose Rock, tie"
    time.sleep(.15)
    displayVar = "Choose a option"
    
def scissorsPlayer():
    print("scissors")
    global score
    global enScore
    global displayVar
    enChoice = random.randrange(1,4)
    print(enChoice)
    displayVar = "thinking"
    time.sleep(.15)
    if(enChoice ==3 ):
        displayVar = "You chose scissors, I chose paper, You Win"
        score += 1
    elif(enChoice == 2):
        displayVar = "You chose scissors, I chose scissors, tie"
    elif(enChoice == 1):
        displayVar = "You chose scissors, I chose Rock, I Win"
        enScore += 1
    time.sleep(.15)
    displayVar = "Choose a option"
    
def paperPlayer():
    print("paper")
    global score
    global enScore
    global displayVar
    enChoice = random.randrange(1,4)
    print(enChoice)
    displayVar = "thinking"
    time.sleep(.15)
    if(enChoice ==3 ):
        displayVar = "You chose paper, I chose paper, tie"
    elif(enChoice == 2):
        displayVar = "You chose paper, I chose scissors, I Win"
        enScore += 1
    elif(enChoice == 1):
        displayVar = "You chose paper, I chose Rock, You Win"
        score += 1
    time.sleep(.15)
    displayVar = "Choose a option"
    
def exitCom():
    exit()


displayVar = StringVar()
displayVar = "Choose a option"

displayScore=tk.Label(root, text=f"You have {score} points, I have {enScore} points",font=('calibre',20,'normal')).pack()
displayGame=tk.Label(root, text=displayVar,font=('calibre',20,'normal')).pack()

rockButton = tk.Button(root,text="Rock", command=rockPlayer).pack()
scissorsButton = tk.Button(root,text="Scissors", command=scissorsPlayer).pack()
paperButton = tk.Button(root,text="Paper", command=paperPlayer).pack()
exitButton = tk.Button(root,text="exit",command=exitCom).pack()

root.mainloop()