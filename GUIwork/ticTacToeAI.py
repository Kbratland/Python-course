import random
import time
from tkinter import *

root = Tk()
root.title("Tic Tac Toe!")
root.configure(bg="light blue")
baseWidth = 150
baseHeight = 225
turnCounter = 0
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
coordX = (screenWidth/2) - (baseWidth/2)
coordY = (screenHeight/2) - (baseHeight/2)
root.geometry('%dx%d+%d+%d' % (baseWidth, baseHeight, coordX, coordY-100))
gameGrid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
Xgoing = True
Playing = True


def takeTurn(buttonIn, cordA, cordB, isPlay):
    global gameGrid
    global Xgoing
    global turnCounter
    if isPlay and buttonIn["text"] == "[ ]":
        if Xgoing:
            turnCounter += 1
            buttonIn.config(text="[X]", background="light green")
            Xgoing = False
            gameGrid[cordA][cordB] = "X"
            time.sleep(0.1)
            aiTurn()
        elif buttonIn["text"] == "[ ]":
            pass
    winCheck(gameGrid)

def aiTurn():
    global gameGrid
    global Xgoing
    global btnList
    global turnCounter
    loopCounter = 0
    if not Xgoing and Playing:
        while True:
            if not Playing:
                break
            # Improved AI: Try to win, block X, else pick random
            # 1. Check if AI can win
            for i in range(3):
                for j in range(3):
                    if gameGrid[i][j] == " ":
                        gameGrid[i][j] = "O"
                        if (
                            (gameGrid[i][0] == gameGrid[i][1] == gameGrid[i][2] == "O") or
                            (gameGrid[0][j] == gameGrid[1][j] == gameGrid[2][j] == "O") or
                            (i == j and gameGrid[0][0] == gameGrid[1][1] == gameGrid[2][2] == "O") or
                            (i + j == 2 and gameGrid[0][2] == gameGrid[1][1] == gameGrid[2][0] == "O")
                        ):
                            aiCordA, aiCordB = i, j
                            gameGrid[i][j] = " "
                            break
                        gameGrid[i][j] = " "
                else:
                    continue
                break
            else:
                # 2. Block X from winning
                for i in range(3):
                    for j in range(3):
                        if gameGrid[i][j] == " ":
                            gameGrid[i][j] = "X"
                            if (
                                (gameGrid[i][0] == gameGrid[i][1] == gameGrid[i][2] == "X") or
                                (gameGrid[0][j] == gameGrid[1][j] == gameGrid[2][j] == "X") or
                                (i == j and gameGrid[0][0] == gameGrid[1][1] == gameGrid[2][2] == "X") or
                                (i + j == 2 and gameGrid[0][2] == gameGrid[1][1] == gameGrid[2][0] == "X")
                            ):
                                aiCordA, aiCordB = i, j
                                gameGrid[i][j] = " "
                                break
                            gameGrid[i][j] = " "
                    else:
                        continue
                    break
                else:
                    # 3. Pick center if available
                    if gameGrid[1][1] == " ":
                        aiCordA, aiCordB = 1, 1
                    else:
                        # 4. Pick random empty
                        winCheck(gameGrid)
                        empty = [(i, j) for i in range(3) for j in range(3) if gameGrid[i][j] == " "]
                        try:
                            aiCordA, aiCordB = random.choice(empty)
                        except IndexError:
                            break
            if(gameGrid[aiCordA][aiCordB] != " "):
                loopCounter += 1
                winCheck(gameGrid)
                if loopCounter > 10:
                    Restart(btnList)
                    break
                continue
            else:
                gameGrid[aiCordA][aiCordB] = "O"
                btnList[aiCordA*3 + aiCordB].config(text="[O]",background="light gray")
                Xgoing = True
                turnCounter += 1
                break
        turnLabel.config(text=" Click ")  
        winCheck(gameGrid)

def winCheck(gIn):
    global Playing
    global turnCounter
    if turnCounter == 9:
        turnLabel.config(text="Draw!")
        Playing = False
    # Horizontal
    if gIn[0][0] == "O" and gIn[0][1] == "O" and gIn[0][2] == "O" or\
            gIn[1][0] == "O" and gIn[1][1] == "O" and gIn[1][2] == "O" or\
            gIn[2][0] == "O" and gIn[2][1] == "O" and gIn[2][2] == "O":
        turnLabel.config(text="O wins")
        Playing = False
    if gIn[0][0] == "X" and gIn[0][1] == "X" and gIn[0][2] == "X" or\
            gIn[1][0] == "X" and gIn[1][1] == "X" and gIn[1][2] == "X" or\
            gIn[2][0] == "X" and gIn[2][1] == "X" and gIn[2][2] == "X":
        turnLabel.config(text="X wins")
        Playing = False
    # Vertical
    if gIn[0][0] == "O" and gIn[1][0] == "O" and gIn[2][0] == "O" or\
            gIn[0][1] == "O" and gIn[1][1] == "O" and gIn[2][1] == "O" or\
            gIn[0][2] == "O" and gIn[1][2] == "O" and gIn[2][2] == "O":
        turnLabel.config(text="O wins")
        Playing = False
    if gIn[0][0] == "X" and gIn[1][0] == "X" and gIn[2][0] == "X" or\
            gIn[0][1] == "X" and gIn[1][1] == "X" and gIn[2][1] == "X" or\
            gIn[0][2] == "X" and gIn[1][2] == "X" and gIn[2][2] == "X":
        turnLabel.config(text="X wins")
        Playing = False
    # Angles
    if gIn[0][0] == "O" and gIn[1][1] == "O" and gIn[2][2] == "O" or\
            gIn[0][2] == "O" and gIn[1][1] == "O" and gIn[2][0] == "O":
        turnLabel.config(text="O wins")
        Playing = False
    if gIn[0][0] == "X" and gIn[1][1] == "X" and gIn[2][2] == "X" or\
            gIn[0][2] == "X" and gIn[1][1] == "X" and gIn[2][0] == "X":
        turnLabel.config(text="X wins")
        Playing = False


def Restart(listIn):
    global gameGrid
    global Playing
    global Xgoing
    global turnCounter
    turnCounter = 0
    for lp in range(len(btnList)):
        btnList[lp].config(text="[ ]",background="light blue")
    for l in range(3):
        for n in range(3):
            gameGrid[l][n] = " "
    turnLabel.config(text=" Click ")
    Xgoing = True
    Playing = True

turnLabel = Label(root, text=" Click ", font=(
    'calibre', 15, 'bold'), bg="light blue", fg="black")

btnA1 = Button(root, text="[ ]",
               command=lambda: takeTurn(btnA1, 0, 0, Playing), bg="light blue", highlightbackground="light blue", highlightcolor="light blue", height=2, width=2)
btnA2 = Button(root, text="[ ]",
               command=lambda: takeTurn(btnA2, 0, 1, Playing), bg="light blue", highlightbackground="light blue", highlightcolor="light blue", height=2, width=2)
btnA3 = Button(root, text="[ ]",
               command=lambda: takeTurn(btnA3, 0, 2, Playing), bg="light blue", highlightbackground="light blue", highlightcolor="light blue", height=2, width=2)
btnB1 = Button(root, text="[ ]",
               command=lambda: takeTurn(btnB1, 1, 0, Playing), bg="light blue", highlightbackground="light blue", highlightcolor="light blue", height=2, width=2)
btnB2 = Button(root, text="[ ]",
               command=lambda: takeTurn(btnB2, 1, 1, Playing), bg="light blue", highlightbackground="light blue", highlightcolor="light blue", height=2, width=2)
btnB3 = Button(root, text="[ ]",
               command=lambda: takeTurn(btnB3, 1, 2, Playing), bg="light blue", highlightbackground="light blue", highlightcolor="light blue", height=2, width=2)
btnC1 = Button(root, text="[ ]",
               command=lambda: takeTurn(btnC1, 2, 0, Playing), bg="light blue", highlightbackground="light blue", highlightcolor="light blue", height=2, width=2)
btnC2 = Button(root, text="[ ]",
               command=lambda: takeTurn(btnC2, 2, 1, Playing), bg="light blue", highlightbackground="light blue", highlightcolor="light blue", height=2, width=2)
btnC3 = Button(root, text="[ ]",
               command=lambda: takeTurn(btnC3, 2, 2, Playing), bg="light blue", highlightbackground="light blue", highlightcolor="light blue", height=2, width=2)

btnList = [btnA1, btnA2, btnA3, btnB1, btnB2, btnB3, btnC1, btnC2, btnC3]

btnPlay = Button(root, text="Reset", command=lambda: Restart(btnList), bg="light blue", highlightbackground="light blue", highlightcolor="light blue")

turnLabel.grid(column=1, row=0)
btnA1.grid(column=0, row=1, padx=5, pady=5)
btnA2.grid(column=1, row=1, padx=5, pady=5)
btnA3.grid(column=2, row=1, padx=5, pady=5)
btnB1.grid(column=0, row=2, padx=5, pady=5)
btnB2.grid(column=1, row=2, padx=5, pady=5)
btnB3.grid(column=2, row=2, padx=5, pady=5)
btnC1.grid(column=0, row=3, padx=5, pady=5)
btnC2.grid(column=1, row=3, padx=5, pady=5)
btnC3.grid(column=2, row=3, padx=5, pady=5)
btnPlay.grid(column=1, row=4)

root.mainloop()
