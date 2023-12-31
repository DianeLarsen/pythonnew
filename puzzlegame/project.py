import random
import tkinter.messagebox
from tkinter import*


def main():
    root = Tk()
    root.geometry("700x300+0+0")
    root.title("Puzzle Games")
    root.configure(background="Black")

    TopsRoot = Frame(root, bg = "Black", pady = 2, width = 800, height = 100, relief = RIDGE)
    TopsRoot.grid(row=0, column=0, columnspan=2)

    lblTitle = Label(TopsRoot, font=('arial', 60, 'bold'), text="Puzzle Games", bd=10, bg="Black", fg="Cornsilk", justify=CENTER)
    lblTitle.grid(row=0, column=0, columnspan=2)

    MainFrame = Frame(root, bg = "Grey", bd = 10, width = 700, height = 200, padx = 2, pady = 3, relief = RIDGE)
    MainFrame.grid(row=1, column=0, padx = 30)

    btn1 = Button(MainFrame, text="Tic Tac Toe", width=30, height = 7, padx = 2, pady = 3, command=open2).grid(row = 0, column = 0)
    btn2 = Button(MainFrame, text="Number Slider", width=30, height = 7, padx = 2, pady = 3, command=open1).grid(row = 0, column = 1)

    
    root.mainloop()

def upDateNumClicks(numClicks):
    global dispClicks
    dispClicks = StringVar()
    dispClicks.set("Num of Clicks" + "\n" + str(numClicks))
def gameStatusUpdate(gameStatus):
    global gameStatusStr
    gameStatusStr = StringVar()
    gameStatusStr.set(gameStatus)
def checker (buttons):
    global click
    click = BooleanVar()
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        open2.scorekeeper()
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        open2.scorekeeper()
def open1():
    top = Toplevel()
    top.geometry("1350x750+0+0")
    top.title("Puzzle Game")
    top.configure(background="Black")
    
    Tops = Frame(top, bg = "Black", pady = 2, width = 1350, height = 100, relief = RIDGE)
    Tops.grid(row=0, column=0)

    lblTitle = Label(Tops, font=('arial', 80, 'bold'), text="Slide Puzzle Game", bd=10, bg="Black", fg="Cornsilk", justify=CENTER)
    lblTitle.grid(row=0, column=0)

    MainFrame = Frame(top, bg = "Grey", bd = 10, width = 1350, height = 600, relief = RIDGE)
    MainFrame.grid(row=1, column=0, padx = 30)

    LeftFrame = Frame(MainFrame, bd = 10, width = 700, height = 500, pady=2, bg = "Black", relief = RIDGE)
    LeftFrame.pack(side=LEFT)

    RightFrame = Frame(MainFrame, bd = 10, width = 540, height = 500, padx=1, pady=2, bg = "Black", relief = RIDGE)
    RightFrame.pack(side=RIGHT)

    RightFrame1 = Frame(RightFrame, bd = 10, width = 540, height = 200, padx=10,pady=2, bg = "Black", relief = RIDGE)
    RightFrame1.grid(row=0, column=0)

    RightFrame2a = Frame(RightFrame, bd = 10, width = 540, height = 140, padx=10,pady=2, bg = "Black", relief = RIDGE)
    RightFrame2a.grid(row=1, column=0)

    RightFrame2b = Frame(RightFrame, bd = 10, width = 540, height = 140, padx=10, pady=2, bg = "Black", relief = RIDGE)
    RightFrame2b.grid(row=2, column=0)
    global numClicks
    numClicks = 0
    global dispClicks
    dispClicks = StringVar()
    dispClicks.set("Num of Clicks" + "\n" + str(numClicks))
    global gameStatusStr
    gameStatusStr = StringVar()



    def gameStatusUpdate(gameStatus):
        global gameStatusStr
        gameStatusStr.set(gameStatus)

    class Btns_:
        def __init__(self, text_, x, y):
            self.enterValue = text_
            self.textEntered = StringVar()
            self.textEntered.set(text_)
            self.x = x
            self.y = y
            self.btnNum = Button(LeftFrame, textvariable=self.textEntered, font=('arial', 80), bd=3, command=lambda i = self.x, j=self.y : emptySpot(i, j))
            self.btnNum.place(x = self.x*170, y = self.y*150, width=165, height=165)
    
    def shuffle():
        global btnNums
        nums = []
        for x in range(12):
            x += 1
            if x == 12:
                nums.append("")
            else:
                nums.append(str(x))

        for y in range(len(btnNums)):
            for x in range(len(btnNums[y])):
                num = random.choice(nums)
                btnNums[y][x].textEntered.set(num)
                nums.remove(num)
        numClicks = 0
        upDateNumClicks()
        gameStatusUpdate("")

    lblClicks = Label(RightFrame1, textvariable=dispClicks, font=('arial', 40)).place(x=0, y=10, width=500, height=160 )
    btnShuf = Button(RightFrame2a, text="New Game", font=('arial', 40), bd=5, command=shuffle).place(x=0, y=10, width=500, height=100 )
    lblScore = Label(RightFrame2b, textvariable=gameStatusStr, font=('arial', 40)).place(x=0, y=10, width=500, height=100 )

    global btnNums
    btnNums = []
    global name
    name = 0

    for y in range(3):
        btnNums_ = []
        for x in range(4):
            name += 1
            if name == 12:
                name = ""
            btnNums_.append(Btns_(str(name), x, y))
        btnNums.append(btnNums_)

    # shuffle()
    def emptySpot(y, x):
        global numClicks, btnNums
        if not btnNums[x][y].textEntered.get() == "":
            for i in range(-1, 2):
                newX = x + i
                if not (newX < 0 or len(btnNums) - 1 < newX or i == 0):
                    if btnNums[newX][y].textEntered.get() == "":
                        text = btnNums[x][y].textEntered.get()
                        btnNums[x][y].textEntered.set(btnNums[newX][y].textEntered.get())
                        btnNums[newX][y].textEntered.set(text)
                        winCheck()
                        break
            for j in range(-1, 2):
                newY = y + j
                if not ((newY < 0) or len(btnNums[0]) - 1 < newY or j == 0):
                    if btnNums[x][newY].textEntered.get() == "":
                        text = btnNums[x][y].textEntered.get()
                        btnNums[x][y].textEntered.set(btnNums[x][newY].textEntered.get())
                        btnNums[x][newY].textEntered.set(text)
                        winCheck()
                        break           
            numClicks += 1
            upDateNumClicks(numClicks)
    def winCheck():
        lost = False
        if numClicks == 0:
            pass
        else:
            for y in range(len(btnNums)):
                for x in range(len(btnNums[y])):
                    if btnNums[y][x].enterValue != btnNums[y][x].textEntered.get():
                        
                        lost = True
                        break
                    if not lost:
                        gameStatusUpdate("You Won!")

def open2():
    top1 = Toplevel()
    top1.geometry("1350x750+0+0")
    top1.title("Tic Tac Toe")
    top1.configure(background="Black")

    Tops = Frame(top1, bg = "Black", pady = 2, width = 1350, height = 100, relief = RIDGE)
    Tops.grid(row=0, column=0)

    lblTitle = Label(Tops, font=('arial', 50, 'bold'), text="Tic Tac Toe", bd=21, bg="Black", fg="Cornsilk", justify=CENTER)
    lblTitle.grid(row=0, column=0)

    MainFrame = Frame(top1, bg = "Grey", bd = 10, width = 1350, height = 600, relief = RIDGE)
    MainFrame.grid(row=1, column=0)

    LeftFrame = Frame(MainFrame, bd = 10, width = 750, height = 500, pady=2, padx = 10,bg = "Black", relief = RIDGE)
    LeftFrame.pack(side=LEFT)

    RightFrame = Frame(MainFrame, bd = 10, width = 560, height = 500, padx=1, pady=2, bg = "Black", relief = RIDGE)
    RightFrame.pack(side=RIGHT)

    RightFrame1 = Frame(RightFrame, bd = 10, width = 560, height = 200, padx=10,pady=2, bg = "Black", relief = RIDGE)
    RightFrame1.grid(row=0, column=0)

    RightFrame2 = Frame(RightFrame, bd = 10, width = 560, height = 200, padx=10,pady=2, bg = "Black", relief = RIDGE)
    RightFrame2.grid(row=1, column=0)
    global PlayerX
    PlayerX = IntVar()
    global PlayerO
    PlayerO = IntVar()

    PlayerX.set(0)
    PlayerO.set(0)
    global buttons
    buttons = StringVar()
    global click
    click = True



    def scorekeeper():
        if button1['text'] == "X" and button2['text'] == "X" and button3['text'] == "X":
            button1.configure(background = 'light green') 
            button2.configure(background = 'light green') 
            button3.configure(background = 'light green') 
            n = float(PlayerX.get())
            score = n + 1
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X", "You have just won a game")
        if button4['text'] == "X" and button5['text'] == "X" and button6['text'] == "X":
            button4.configure(background = 'light green') 
            button5.configure(background = 'light green') 
            button6.configure(background = 'light green') 
            n = float(PlayerX.get())
            score = n + 1
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X", "You have just won a game")
        if button7['text'] == "X" and button8['text'] == "X" and button9['text'] == "X":
            button7.configure(background = 'light green') 
            button8.configure(background = 'light green') 
            button9.configure(background = 'light green') 
            n = float(PlayerX.get())
            score = n + 1
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X", "You have just won a game")
        if button1['text'] == "X" and button4['text'] == "X" and button7['text'] == "X":
            button1.configure(background = 'light green') 
            button4.configure(background = 'light green') 
            button7.configure(background = 'light green') 
            n = float(PlayerX.get())
            score = n + 1
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X", "You have just won a game")
        if button2['text'] == "X" and button5['text'] == "X" and button8['text'] == "X":
            button2.configure(background = 'light green') 
            button5.configure(background = 'light green') 
            button8.configure(background = 'light green') 
            n = float(PlayerX.get())
            score = n + 1
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X", "You have just won a game")
        if button3['text'] == "X" and button6['text'] == "X" and button9['text'] == "X":
            button3.configure(background = 'light green') 
            button6.configure(background = 'light green') 
            button9.configure(background = 'light green') 
            n = float(PlayerX.get())
            score = n + 1
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X", "You have just won a game")
        if button1['text'] == "X" and button5['text'] == "X" and button9['text'] == "X":
            button1.configure(background = 'light green') 
            button5.configure(background = 'light green') 
            button9.configure(background = 'light green') 
            n = float(PlayerX.get())
            score = n + 1
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X", "You have just won a game")
        if button3['text'] == "X" and button5['text'] == "X" and button7['text'] == "X":
            button3.configure(background = 'light green') 
            button5.configure(background = 'light green') 
            button7.configure(background = 'light green') 
            n = float(PlayerX.get())
            score = n + 1
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X", "You have just won a game")

        # Player O
        if button1['text'] == "O" and button2['text'] == "O" and button3['text'] == "O":
            button1.configure(background = 'pale violet red') 
            button2.configure(background = 'pale violet red') 
            button3.configure(background = 'pale violet red') 
            n = float(PlayerO.get())
            score = n + 1
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O", "You have just won a game")
        if button4['text'] == "O" and button5['text'] == "O" and button6['text'] == "O":
            button4.configure(background = 'pale violet red') 
            button5.configure(background = 'pale violet red') 
            button6.configure(background = 'pale violet red') 
            n = float(PlayerO.get())
            score = n + 1
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O", "You have just won a game")
        if button7['text'] == "O" and button8['text'] == "O" and button9['text'] == "O":
            button7.configure(background = 'pale violet red') 
            button8.configure(background = 'pale violet red') 
            button9.configure(background = 'pale violet red') 
            n = float(PlayerO.get())
            score = n + 1
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O", "You have just won a game")
        if button1['text'] == "O" and button4['text'] == "O" and button7['text'] == "O":
            button1.configure(background = 'pale violet red') 
            button4.configure(background = 'pale violet red') 
            button7.configure(background = 'pale violet red') 
            n = float(PlayerO.get())
            score = n + 1
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O", "You have just won a game")
        if button2['text'] == "O" and button5['text'] == "O" and button8['text'] == "O":
            button2.configure(background = 'pale violet red') 
            button5.configure(background = 'pale violet red') 
            button8.configure(background = 'pale violet red') 
            n = float(PlayerO.get())
            score = n + 1
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O", "You have just won a game")
        if button3['text'] == "O" and button6['text'] == "O" and button9['text'] == "O":
            button3.configure(background = 'pale violet red') 
            button6.configure(background = 'pale violet red') 
            button9.configure(background = 'pale violet red') 
            n = float(PlayerO.get())
            score = n + 1
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O", "You have just won a game")
        if button1['text'] == "O" and button5['text'] == "O" and button9['text'] == "O":
            button1.configure(background = 'pale violet red') 
            button5.configure(background = 'pale violet red') 
            button9.configure(background = 'pale violet red') 
            n = float(PlayerO.get())
            score = n + 1
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O", "You have just won a game")
        if button3['text'] == "O" and button5['text'] == "O" and button7['text'] == "O":
            button3.configure(background = 'pale violet red') 
            button5.configure(background = 'pale violet red') 
            button7.configure(background = 'pale violet red') 
            n = float(PlayerO.get())
            score = n + 1
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O", "You have just won a game")

    def reset():
        button1['text'] = " " 
        button2['text'] = " " 
        button3['text'] = " " 
        button4['text'] = " " 
        button5['text'] = " " 
        button6['text'] = " " 
        button7['text'] = " " 
        button8['text'] = " " 
        button9['text'] = " " 
        button1.configure(background = 'gainsboro') 
        button2.configure(background = 'gainsboro') 
        button3.configure(background = 'gainsboro') 
        button4.configure(background = 'gainsboro') 
        button5.configure(background = 'gainsboro') 
        button6.configure(background = 'gainsboro') 
        button7.configure(background = 'gainsboro') 
        button8.configure(background = 'gainsboro') 
        button9.configure(background = 'gainsboro') 

    def newGame():
        reset()
        PlayerX.set(0)
        PlayerO.set(0)



    lblPlayerX = Label(RightFrame1, font=('arial', 40, 'bold'), text = "Player X :", width = 8, padx = 2, pady = 2, bg = "light green")
    lblPlayerX.grid(row = 0, column = 0, sticky = W)

    txtPlayerX = Entry(RightFrame1, font=('arial', 40, 'bold'), bd = 2, fg = 'Grey', textvariable = PlayerX, width = 6, justify = LEFT).grid(row = 0, column = 1)

    lblPlayerO = Label(RightFrame1, font=('arial', 40, 'bold'), text = "Player O :", width = 8,padx = 2, pady = 2, bg = 'pale violet red')
    lblPlayerO.grid(row = 1, column = 0, sticky = W)

    txtPlayerO = Entry(RightFrame1, font=('arial', 40, 'bold'), bd = 2, fg = 'Grey', textvariable = PlayerO, width = 6, justify = LEFT).grid(row = 1, column = 1)

    btnReset = Button(RightFrame2, text="Reset", font=('arial', 40, 'bold'), height = 1, width = 13, command = reset)
    btnReset.grid(row = 0, column = 0, padx = 6, pady = 10)

    btnNewGame = Button(RightFrame2, text="New Game", font=('arial', 40, 'bold'), height = 1, width = 13, command = newGame)
    btnNewGame.grid(row = 1, column = 0, padx = 6, pady = 10)


    button1 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width = 8, bg="gainsboro", command = lambda:checker(button1))
    button1.grid(row = 1, column = 0, sticky = S+N+E+W)

    button2 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width = 8, bg="gainsboro", command = lambda:checker(button2))
    button2.grid(row = 1, column = 1, sticky = S+N+E+W)

    button3 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width = 8, bg="gainsboro", command = lambda:checker(button3))
    button3.grid(row = 1, column = 2, sticky = S+N+E+W)

    button4 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width = 8, bg="gainsboro", command = lambda:checker(button4))
    button4.grid(row = 2, column = 0, sticky = S+N+E+W)

    button5 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width = 8, bg="gainsboro", command = lambda:checker(button5))
    button5.grid(row = 2, column = 1, sticky = S+N+E+W)

    button6 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width = 8, bg="gainsboro", command = lambda:checker(button6))
    button6.grid(row = 2, column = 2, sticky = S+N+E+W)

    button7 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width = 8, bg="gainsboro", command = lambda:checker(button7))
    button7.grid(row = 3, column = 0, sticky = S+N+E+W)

    button8 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width = 8, bg="gainsboro", command = lambda:checker(button8))
    button8.grid(row = 3, column = 1, sticky = S+N+E+W)

    button9 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 3, width = 8, bg="gainsboro", command = lambda:checker(button9))
    button9.grid(row = 3, column = 2, sticky = S+N+E+W)





if __name__ == "__main__":
    main()