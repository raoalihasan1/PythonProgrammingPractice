from tkinter import Tk, PhotoImage, Button, messagebox
def CreateButtons():
    square[0] = Button(window, image = availablespace, width = "100", height = "100", command = lambda: HandleButtonClick(0))
    square[0].place(x = 0, y = 0)
    square[1] = Button(window, image = availablespace, width = "100", height = "100", command = lambda: HandleButtonClick(1))
    square[1].place(x = 100, y = 0)
    square[2] = Button(window, image = availablespace, width = "100", height = "100", command = lambda: HandleButtonClick(2))
    square[2].place(x = 200, y = 0)
    square[3] = Button(window, image = availablespace, width = "100", height = "100", command = lambda: HandleButtonClick(3))
    square[3].place(x = 0, y = 100)
    square[4] = Button(window, image = availablespace, width = "100", height = "100", command = lambda: HandleButtonClick(4))
    square[4].place(x = 100, y = 100)
    square[5] = Button(window, image = availablespace, width = "100", height = "100", command = lambda: HandleButtonClick(5))
    square[5].place(x = 200, y = 100)
    square[6] = Button(window, image = availablespace, width = "100", height = "100", command = lambda: HandleButtonClick(6))
    square[6].place(x = 0, y = 200)
    square[7] = Button(window, image = availablespace, width = "100", height = "100", command = lambda: HandleButtonClick(7))
    square[7].place(x = 100, y = 200)
    square[8] = Button(window, image = availablespace, width = "100", height = "100", command = lambda: HandleButtonClick(8))
    square[8].place(x = 200, y = 200)
def CheckWin():
    Won = []
    Won.append(oxo[0][0] == oxo[0][1] == oxo[2][2] and oxo [0][0] != '')
    Won.append(oxo[0][2] == oxo[1][1] == oxo[2][0] and oxo[0][2] != '')
    for i in range(3):
        Won.append(oxo[i][0] == oxo[i][1] == oxo[i][2] and oxo[i][0] != '')
        Won.append(oxo[0][i] == oxo[1][i] == oxo[2][i] and oxo[0][i] != '')
        if True in Won:
            WinButton = Button(window, image = winner, width = "300", height = "100")
            WinButton.pack()
def UpdateMove(SquareNum, PlayerNum):
    SquareToMap = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    m = SquareToMap
    p = PlayerNum
    s = SquareNum
    oxo[m[s][0]][m[s][1]] = p
    CheckWin()
def SquareTaken():
    messagebox.showinfo("Square Taken", "This Square Is Already Taken Please Choose Another!")
def HandleButtonClick(ButtonNumber):
    global Counter
    print("Button", ButtonNumber, "Was Clicked")
    if Counter % 2 == 0:
        square[ButtonNumber].configure(image = player1, command = SquareTaken)
        UpdateMove(ButtonNumber, 1)
    else:
        square[ButtonNumber].configure(image = player2, command = SquareTaken)
        UpdateMove(ButtonNumber, 2)
    Counter += 1
window = Tk()
window.title("OXO Game")
window.geometry("300x300")
availablespace = PhotoImage(file = "myButton.png")
player1 = PhotoImage(file = "myButtonP1.png")
player2 = PhotoImage(file = "myButtonP2.png")
winner = PhotoImage(file = "winner.png")
square = [None]*9
Counter = 0
CreateButtons()
oxo = [
    ['','',''],
    ['','',''],
    ['','','']
]
window.mainloop()
