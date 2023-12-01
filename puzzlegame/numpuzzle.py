import random
from tkinter import*

root = Tk()
root.geometry("1350x750+0+0")
root.title("Puzzle Game")
root.configure(background="Black")

Tops = Frame(root, bg = "Black", pady = 2, width = 1350, height = 100, relief = RIDGE)
Tops.grid(row=0, column=0)

lblTitle = Label(Tops, font=('arial', 80, 'bold'), text="Slide Puzzle Game", bd=10, bg="Black", fg="Cornsilk", justify=CENTER)
lblTitle.grid(row=0, column=0)

MainFrame = Frame(root, bg = "Grey", bd = 10, width = 1350, height = 600, relief = RIDGE)
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

numClicks = 0
dispClicks = StringVar()
dispClicks.set("# of Clicks" + "\n" + "0")

gameStatusStr = StringVar()

def upDateNumClicks():
    global numClicks, dispClicks
    dispClicks.set("Num of Clicks" + "\n" + str(numClicks))

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
    global numClicks, btnNums
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

btnNums = []
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
        upDateNumClicks()
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
root.mainloop()