import random
from tkinter import *

root = Tk()
root.title("Tic Tac Toe!")
root.configure(bg="light blue")
baseWidth = 200
baseHeight = 250
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
    if isPlay and buttonIn["text"] == "[ ]":
        #and buttonIn["text"] == "[ ]"
        if Xgoing:
            buttonIn.config(text="[X]")
            turnLabel.config(text="AI's Turn")
            Xgoing = False
            gameGrid[cordA][cordB] = "X"
            for lp in range(3):
                print(gameGrid[lp])
            print("")
            # buttonIn["text"] == "[ ]"
        elif buttonIn["text"] == "[ ]":
            pass
    winCheck(gameGrid)

def aiTurn():
    global gameGrid
    global Xgoing
    global btnList
    if not Xgoing and Playing:
        while True:
            aiCordA = random.randint(0, 2)
            aiCordB = random.randint(0, 2)
            if(gameGrid[aiCordA][aiCordB] != " "):
                continue
            else:
                gameGrid[aiCordA][aiCordB] = "O"
                btnList[aiCordA*3 + aiCordB].config(text="[O]")
                Xgoing = True
                break
        turnLabel.config(text="X's Turn")  
        winCheck(gameGrid)
        for lp in range(3):
            print(gameGrid[lp])

def winCheck(gIn):
    global Playing
    # Horizontal
    if gIn[0][0] == "O" and gIn[0][1] == "O" and gIn[0][2] == "O" or\
            gIn[1][0] == "O" and gIn[1][1] == "O" and gIn[1][2] == "O" or\
            gIn[2][0] == "O" and gIn[2][1] == "O" and gIn[2][2] == "O":
        turnLabel.config(text="O wins!")
        print("---O Wins - Horizontal ---\n")
        Playing = False
    if gIn[0][0] == "X" and gIn[0][1] == "X" and gIn[0][2] == "X" or\
            gIn[1][0] == "X" and gIn[1][1] == "X" and gIn[1][2] == "X" or\
            gIn[2][0] == "X" and gIn[2][1] == "X" and gIn[2][2] == "X":
        turnLabel.config(text="X wins!")
        print("---X Wins - Horizontal---\n")
        Playing = False
    # Vertical
    if gIn[0][0] == "O" and gIn[1][0] == "O" and gIn[2][0] == "O" or\
            gIn[0][1] == "O" and gIn[1][1] == "O" and gIn[2][1] == "O" or\
            gIn[0][2] == "O" and gIn[1][2] == "O" and gIn[2][2] == "O":
        turnLabel.config(text="O wins!")
        print("---O Wins - Vertical---\n")
        Playing = False
    if gIn[0][0] == "X" and gIn[1][0] == "X" and gIn[2][0] == "X" or\
            gIn[0][1] == "X" and gIn[1][1] == "X" and gIn[2][1] == "X" or\
            gIn[0][2] == "X" and gIn[1][2] == "X" and gIn[2][2] == "X":
        turnLabel.config(text="X wins!")
        print("---X Wins - Vertical---\n")
        Playing = False
    # Angles
    if gIn[0][0] == "O" and gIn[1][1] == "O" and gIn[2][2] == "O" or\
            gIn[0][2] == "O" and gIn[1][1] == "O" and gIn[2][0] == "O":
        turnLabel.config(text="O wins!")
        print("---O Wins - Angled---\n")
        Playing = False
    if gIn[0][0] == "X" and gIn[1][1] == "X" and gIn[2][2] == "X" or\
            gIn[0][2] == "X" and gIn[1][1] == "X" and gIn[2][0] == "X":
        turnLabel.config(text="X wins!")
        print("---X Wins - Angled---\n")
        Playing = False


def Restart(listIn):
    global gameGrid
    global Playing
    global Xgoing
    print("\n---Restarting---\n")
    for lp in range(len(btnList)):
        btnList[lp].config(text="[ ]")
    for l in range(3):
        for n in range(3):
            gameGrid[l][n] = " "
    turnLabel.config(text="X's Turn")
    Xgoing = True
    Playing = True
    for lp in range(3):
        print(gameGrid[lp])
    print("")


turnLabel = Label(root, text="X's Turn", font=(
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

btnAI = Button(root, text="AI", command=lambda: aiTurn(), bg="light blue", highlightbackground="light blue", highlightcolor="light blue")

turnLabel.grid(column=1, row=0, sticky="nsew")
btnA1.grid(column=0, row=1, sticky="nsew", padx=5, pady=5)
btnA2.grid(column=1, row=1,)
btnA3.grid(column=2, row=1, sticky="nsew", padx=5, pady=5)
btnB1.grid(column=0, row=2, sticky="nsew", padx=5, pady=5)
btnB2.grid(column=1, row=2,)
btnB3.grid(column=2, row=2, sticky="nsew", padx=5, pady=5)
btnC1.grid(column=0, row=3, sticky="nsew", padx=5, pady=5)
btnC2.grid(column=1, row=3,)
btnC3.grid(column=2, row=3, sticky="nsew", padx=5, pady=5)
btnPlay.grid(column=1, row=4, sticky="nsew")
btnAI.grid(column=1, row=5, sticky="nsew")

root.mainloop()
