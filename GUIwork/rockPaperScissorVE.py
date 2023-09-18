import random
from tkinter import *

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("350x165")

 
text = StringVar() 
scoreText = StringVar
score = 0
enScore = 0
def rock():
    global text
    global scoreText
    global score
    global enScore
    
    enChoice = random.randrange(0,7)
    if(enChoice == 1 or enChoice == 4):
        text = "You picked rock, I picked rock, Tie, Play again?"
    elif(enChoice == 2 or enChoice == 5):
        text = "You picked rock, I picked paper, I Win, Play again?"
        enScore += 1
    else:
        text = "You picked rock, I picked Scissors, You Win, Play again?"
        score += 1
        
    scoreText = f"You have {score} points, I have {enScore} points"
    scoreLabel.config(text = scoreText)
    gameLabel.config(text = text)
def paper():
    global text
    global scoreText
    global score
    global enScore
    
    enChoice = random.randrange(0,7)
    if(enChoice == 1 or enChoice == 4):
        text = "You picked paper, I picked rock, You Win, Play again?"
        score += 1
    elif(enChoice == 2 or enChoice == 5):
        text = "You picked paper, I picked paper, Tie, Play again?"
    else:
        text = "You picked paper, I picked Scissors, I Win, Play again?"
        enScore += 1
        
    scoreText = f"You have {score} points, I have {enScore} points"
    scoreLabel.config(text = scoreText)
    gameLabel.config(text = text)
def scissors():
    global text
    global scoreText
    global score
    global enScore
    
    enChoice = random.randrange(0,7)
    if(enChoice == 1 or enChoice == 4):
        text = "You picked scissors, I picked rock, I Win, Play again?"
        enScore += 1
    elif(enChoice == 2 or enChoice == 5):
        text = "You picked scissors, I picked paper, You Win, Play again?"
        score += 1
    else:
        text = "You picked scissors, I picked Scissors, Tie, Play again?"
        
    scoreText = f"You have {score} points, I have {enScore} points"    
    scoreLabel.config(text = scoreText)
    gameLabel.config(text = text)
def quitGame():
    exit()
scoreLabel = Label(root,text = f"You have {score} points, I have {score} points")
gameLabel = Label(root,text = "I will pick when you do")

rockButton = Button(root,text = "Rock",command = rock)
paperButton = Button(root,text = "Paper",command = paper)
scissorButton = Button(root,text = "Scissors",command = scissors)
exitButton = Button(root, text="Exit",command=quitGame)

scoreLabel.pack()
gameLabel.pack()
rockButton.pack()
paperButton.pack()
scissorButton.pack()
exitButton.pack()

root.mainloop()