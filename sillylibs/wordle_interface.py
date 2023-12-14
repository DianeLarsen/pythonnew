from tkinter import*    
from wordle import Wordle
import tkinter.messagebox
import random

top2 = Tk()

# top2 = Toplevel()
top2.title("WordlePy")
top2.geometry('535x800+0+0')  
top2.configure(background="black")
Tops2 = Frame(top2, bg = "Black", pady = 2, width = 1350, height = 90, relief = RIDGE)
Tops2.grid(row=0, column=0)
lblTitle = Label(Tops2, font=('arial', 30, 'bold'), text="Wordle Py", bd=10, bg="Black", fg="Cornsilk", justify=CENTER)
lblTitle.grid(row=0, column=0)
MainFrame1 = Frame(top2, bg = "Grey", bd = 10, width = 450, height = 490, padx = 2, pady = 3, relief = RIDGE)
MainFrame1.grid(row=1, column=0, padx = 30)
# LeftFrame = Frame(MainFrame1, bd = 10, width = 100, height = 500, pady=2, bg = "Black" )
# LeftFrame.pack(side=LEFT)
RightFrame = Frame(MainFrame1, bd = 10, width = 450, height = 525, padx=1, pady=2, bg = "Black" )
RightFrame.pack(anchor=CENTER)
BottomFrame = Frame(MainFrame1, bd = 10, width = 450, height = 150, padx=1, pady=3, bg = "Black")
BottomFrame.pack(side=BOTTOM)
def assignLtr(ltr, ltrBtn):
    test = top2.focus_get()
    test.configure(bg="lavender")
    # test.select_range(0, END)
    test.insert(0, ltr.get())
    if test == newword5:
        EnterButton.focus()
        EnterButton.configure(bg="Green")
        test = top2.focus_get()
    elif test == newword4:
        newword5.focus()
        test = top2.focus_get()
    elif test == newword3:
        newword4.focus()
        test = top2.focus_get()
    elif test == newword2:
        newword3.focus()  
        test = top2.focus_get()
    elif test == newword1:
        newword2.focus()  
        test = top2.focus_get()
    else:  
        test = top2.focus_get()
    
def validate_ltr(ltr):
    ltrs = ltr.get()
    if ltrs:
        if ltrs.isalpha():
            if len(ltrs) == 1:
                ltr.delete(0, END)
                ltr.insert(0, ltrs.upper())
                return True
            else:
                tkinter.messagebox.showinfo("Error", f"Must only be 1 character per box!")
                return False
        else:
            tkinter.messagebox.showinfo("Error", f"Letter Characters Only")
            return False
    elif ltrs == "":
        return True
def restart():
    global word_set, secret, wordle, lettersMatchedGreen, lettersMatchedOrange
    word_set = load_word_set("words.txt")
    secret = random.choice(list(word_set))
    wordle = Wordle(secret)
    print(secret)
    wordle.attempts = []
    lettersMatchedGreen = []
    lettersMatchedOrange = []
    assignColor()
    writeboxes()

def clear():
    writeboxes()

def backspace():
    test = top2.focus_get()
    if test == EnterButton:
        
        newword5.focus()
        test = top2.focus_get()
        test.delete(0, END)
    elif test == newword5:
        newword4.focus()
        test = top2.focus_get()
        test.delete(0, END)
    elif test == newword4:
        newword3.focus()
        test = top2.focus_get()
        test.delete(0, END)
    elif test == newword3:
        newword2.focus()
        test = top2.focus_get()
        test.delete(0, END)
    elif test == newword2:
        newword1.focus()  
        test = top2.focus_get()
        test.delete(0, END)      
    else:  
        test = top2.focus_get()
        if test == EnterButton:
            newword5.focus()
            test = top2.focus_get()
            test.delete(0, END)
    test = top2.focus_get()


class Btns_:
    def __init__(self, text_, x, y):
        self.enterValue = text_
        self.textEntered = StringVar()
        self.textEntered.set(text_)
        self.x = x
        self.y = y
        self.btnNum = Button(RightFrame, textvariable=self.textEntered, font=('arial', 20), bd=3, bg="LightSteelBlue4", relief = GROOVE, takefocus=0)
        self.btnNum.place(x = self.x*70, y = self.y*70, width=60, height=60)
class Boxes_:
    def __init__(self,text_, color, x, y):
        self.enterValue = text_
        self.textEntered = StringVar()
        self.textEntered.set(text_)
        self.x = x
        self.y = y
        self.color = color
        self.btnNum = Label(RightFrame, textvariable=self.textEntered, bg=color, font=('arial', 20), bd=3, relief = GROOVE, takefocus=0)
        self.btnNum.place(x = self.x*70, y = self.y*70, width=60, height=60)
class InPuts_:
    def __init__(self, text_, x, y):
        self.enterValue = text_
        self.textEntered = StringVar()
        self.textEntered.set(self.enterValue)
        self.x = x
        self.y = y
        self.btnNum = Entry(RightFrame, font=('arial', 20), bd=3, justify=CENTER, relief = GROOVE, validatecommand=lambda: validate_ltr(self.btnNum),validate="focusout", invalidcommand=backspace)

        self.btnNum.place(x = self.x*70, y = self.y*70, width=60, height=60)
    def __repr__(self):
        return f"{self.textEntered}"
    def attempt(self, word: str):
        word = word.upper()
        self.attempts.append(word)
class LtrBtns_:
    def __init__(self, text_, color, x, y):
        self.enterValue = text_
        self.textEntered = StringVar()
        self.textEntered.set(text_)
        self.color = color
        self.x = x
        self.y = y
        self.btnNum = Button(BottomFrame, textvariable=self.textEntered, font=('arial', 20), bd=2, bg=self.color, relief = GROOVE, command=lambda ltr=self.textEntered: assignLtr(ltr, self.btnNum))
        # self.btnNum.bind("<FocusIn>", changeColor)
        self.btnNum.place(x = self.x*40, y = self.y*40, width=35, height=35)
letters = ["QWERTYUIOP","ASDFGHJKL ","ZXCVBNM   "]

def assignColor():
    global ltrcolor
    ltrcolor = [[] for i in range(3)]
    for i in range(3):
        for j in range(10):
            ltrcolor[i].append("LightSteelBlue1")
    
btnNums = []
btnLetts = []
name = ""
newWord_ = []
guesses = []
newword1 = ""
newword2 = ""
newword3 = ""
newword4 = ""
newword5 = ""
lettersPicked = []

def writeboxes():
    global newWord_, newword1, newword2, newword3, newword4, newword5
    for y in range(len(wordle.attempts)):
        btnNums_ = []
        for x in range(5):
            btnNums_.append(Boxes_(str(wordle.attempts[y][x]), str(wordle.color[y][x]), x+0.50, y))
        btnNums.append(btnNums_)
    if len(wordle.attempts) < 6 and not wordle.is_solved:
        for y in range(len(wordle.attempts), len(wordle.attempts) + 1):
            
            newWord_ = []
            for x in range(5):
                newWord_.append(InPuts_(str(name), x+0.50, y))
            guesses.append(newWord_)
    if len(wordle.attempts) < 6:
        for y in range(len(wordle.attempts)+1, 6):
            btnNums_ = []
            for x in range(5):
                btnNums_.append(Btns_(str(name), x+0.50, y))
            btnNums.append(btnNums_)
        for y in range(3):
            global btnLett_
            btnLett_ = []
            for x in range(10):
                letterKey = letters[y][x]
                if letterKey != " ":
                    btnLett_.append(LtrBtns_(str(letters[y][x]), str(ltrcolor[y][x]), (x+0.50+(y/2)), y))
            btnLetts.append(btnLett_)
    newword1 = newWord_[0].btnNum
    newword2 = newWord_[1].btnNum
    newword3 = newWord_[2].btnNum
    newword4 = newWord_[3].btnNum
    newword5 = newWord_[4].btnNum
    newword1.focus()

    
# for y in range(6):
#     btnNums_ = []
#     for x in range(5):
#         btnNums_.append(Btns_(str(name), x+0.50, y))
#     btnNums.append(btnNums_)
def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
        return word_set

word_set = load_word_set("wordle_words.txt")
secret = random.choice(list(word_set))
wordle = Wordle(secret)
print(secret)
result = ""
ltrcolor = []
lettersMatchedGreen = []
lettersMatchedOrange = []
def checkLtrColor():
    global i, j, lettersMatchedGreen, lettersMatchedOrange
    for k in range(len(lettersPicked)):
        for i in range(3):
            try:
                j = letters[i].index(lettersPicked[k])
                if letters[i][j] in secret:
                    if lettersPicked[k] == secret[k]:
                        ltrcolor[i][j] = "Green"
                        lettersMatchedGreen.append(letters[i][j])
                    elif lettersPicked[k] not in lettersMatchedGreen and lettersPicked[k] not in lettersMatchedOrange:
                        ltrcolor[i][j] = "Orange"
                        lettersMatchedOrange.append(letters[i][j])
                elif letters[i][j] not in lettersMatchedOrange and letters[i][j] not in lettersMatchedGreen:
                    ltrcolor[i][j] = "LightSteelBlue4"
            except:
                pass

def checkGuess(char1, char2, char3, char4, char5):
    global lettersPicked
    lettersPicked = []
    chars = [char1, char2, char3, char4, char5]
    for char in chars:
        lettersPicked.append(char)
    if "" in chars:
        tkinter.messagebox.showinfo("Error", "You must enter 1 letter per box!")
        return
    x = "".join(chars).upper()
    if len(x) != wordle.WORD_LENGTH:
        tkinter.messagebox.showinfo("Error", f"Word must be {wordle.WORD_LENGTH} characters")
        return
    if not x in word_set:
        tkinter.messagebox.showinfo("Error", f"{x} is not a valid word")
        newword1.focus()
        return
    wordle.attempt(x)
    result = wordle.guess(x)
    checkLtrColor()
    writeboxes()
    

    if wordle.is_solved:
        tkinter.messagebox.showinfo("Winner!", f"You've solved the puzzle in {len(wordle.attempts)} tries, the secet word was: {secret}!")
    elif not wordle.can_attempt:
        tkinter.messagebox.showinfo("Try Again", f"You failed to solve the puzzle in 6 attempts, the secet word was: {secret}")
assignColor()

writeboxes()

newword1 = newWord_[0].btnNum
newword2 = newWord_[1].btnNum
newword3 = newWord_[2].btnNum
newword4 = newWord_[3].btnNum
newword5 = newWord_[4].btnNum


ClearButton  = Button(RightFrame, text="Clear", background="LightSteelBlue4", font=('Calibri', 16, 'bold'),padx = 3, pady = 3, command=clear)  
ClearButton.place(x=60, y=425)  

EnterButton  = Button(RightFrame, text="Enter", background="LightSteelBlue4", font=('Calibri', 16, 'bold'),padx = 3, pady = 3, command=lambda:checkGuess(newword1.get(), newword2.get(), newword3.get(), newword4.get(), newword5.get()))  
EnterButton.place(x=155, y=425)  

BackspaceButton  = Button(RightFrame, text="BKSPC", background="LightSteelBlue4", font=('Calibri', 16, 'bold'),padx = 3, pady = 3, command=backspace)  
BackspaceButton.place(x=255, y=425)  

ResetButton  = Button(RightFrame, text="New Game", background="LightSteelBlue4", font=('Calibri', 16, 'bold'),padx = 3, pady = 3, command=restart)  
ResetButton.place(x=125, y=475)  

top2.mainloop()