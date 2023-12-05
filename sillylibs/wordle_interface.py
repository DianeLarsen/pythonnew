from tkinter import*    
from wordle import Wordle
import tkinter.messagebox
import random



top2 = Tk()





# top2 = Toplevel()
top2.title("WordlePy")
top2.geometry('500x600+0+0')  
top2.configure(background="black")
Tops2 = Frame(top2, bg = "Black", pady = 2, width = 1350, height = 90, relief = RIDGE)
Tops2.grid(row=0, column=0)
lblTitle = Label(Tops2, font=('arial', 30, 'bold'), text="Wordle Py", bd=10, bg="Black", fg="Cornsilk", justify=CENTER)
lblTitle.grid(row=0, column=0)
MainFrame1 = Frame(top2, bg = "Grey", bd = 10, width = 450, height = 490, padx = 2, pady = 3, relief = RIDGE)
MainFrame1.grid(row=1, column=0, padx = 30)
# LeftFrame = Frame(MainFrame1, bd = 10, width = 100, height = 500, pady=2, bg = "Black" )
# LeftFrame.pack(side=LEFT)
RightFrame = Frame(MainFrame1, bd = 10, width = 425, height = 490, padx=1, pady=2, bg = "Black" )
RightFrame.pack(side=RIGHT)


class Btns_:
    def __init__(self, text_, x, y):
        self.enterValue = text_
        self.textEntered = StringVar()
        self.textEntered.set(text_)
        self.x = x
        self.y = y
        self.btnNum = Button(RightFrame, textvariable=self.textEntered, font=('arial', 20), bd=3, bg="LightSteelBlue4", relief = GROOVE)
        self.btnNum.place(x = self.x*70, y = self.y*70, width=60, height=60)
class Boxes_:
    def __init__(self,text_, color, x, y):
        self.enterValue = text_
        self.textEntered = StringVar()
        self.textEntered.set(text_)
        self.x = x
        self.y = y
        self.color = color
        self.btnNum = Label(RightFrame, textvariable=self.textEntered, bg=color, font=('arial', 20), bd=3, relief = GROOVE)
        self.btnNum.place(x = self.x*70, y = self.y*70, width=60, height=60)
class InPuts_:
    def __init__(self, text_, x, y):
        self.enterValue = text_
        self.textEntered = StringVar()
        self.textEntered.set(text_)
        self.x = x
        self.y = y
        self.btnNum = Entry(RightFrame, font=('arial', 20), bd=3, relief = GROOVE)
        # self.btnNum['validatecommand'] = (self.btnNum.register(on_validate), '%P')
        
        self.btnNum.place(x = self.x*70, y = self.y*70, width=60, height=60)
    def __repr__(self):
        return f"{self.textEntered}"
    def attempt(self, word: str):
        word = word.upper()
        self.attempts.append(word)

btnNums = []
name = ""
newWord_ = []
guesses = []
newword1 = ""
newword2 = ""
newword3 = ""
newword4 = ""
newword5 = ""
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
    newword1 = newWord_[0].btnNum
    newword2 = newWord_[1].btnNum
    newword3 = newWord_[2].btnNum
    newword4 = newWord_[3].btnNum
    newword5 = newWord_[4].btnNum
    
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

word_set = load_word_set("words.txt")
secret = random.choice(list(word_set))
wordle = Wordle(secret)
print(secret)
result = ""
def checkGuess(char1, char2, char3, char4, char5):
    chars = [char1, char2, char3, char4, char5]
    if "" in chars:
        tkinter.messagebox.showinfo("Error", "You must enter 1 letter per box!")
        return
    x = "".join(chars).upper()

    print(x)
    if len(x) != wordle.WORD_LENGTH:
        tkinter.messagebox.showinfo("Error", f"Word must be {wordle.WORD_LENGTH} characters")
        return
    if not x in word_set:
        tkinter.messagebox.showinfo("Error", f"{x} is not a valid word")
        return
    wordle.attempt(x)
    result = wordle.guess(x)
    # print("results")
    # print(*result, sep="\n")

    
    # print(wordle.attempts)
    
    writeboxes()
    

    if wordle.is_solved:
        tkinter.messagebox.showinfo("Winner!", f"You've solved the puzzle in {len(wordle.attempts)} tries, the secet word was: {secret}!")
    elif not wordle.can_attempt:
        tkinter.messagebox.showinfo("Try Again", f"You failed to solve the puzzle in 6 attempts, the secet word was: {secret}")

writeboxes()

newword1 = newWord_[0].btnNum
newword2 = newWord_[1].btnNum
newword3 = newWord_[2].btnNum
newword4 = newWord_[3].btnNum
newword5 = newWord_[4].btnNum
def restart():
    wordle.attempts = []
    writeboxes()

EnterButton1  = Button(RightFrame, text="Enter", background="LightSteelBlue4", font=('Calibri', 16, 'bold'),padx = 3, pady = 3, command=lambda:checkGuess(newword1.get(), newword2.get(), newword3.get(), newword4.get(), newword5.get()))  
EnterButton1.place(x=165, y=425)  

ResetButton  = Button(RightFrame, text="Reset", background="LightSteelBlue4", font=('Calibri', 16, 'bold'),padx = 3, pady = 3, command=restart)  
ResetButton.place(x=265, y=425)  
# second through 6th columns will have boxes for attepts not editable
# below attempts will be boxes for entry
# below will be blank no boxes



top2.mainloop()