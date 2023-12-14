#Source for madlibs: https://www.glowwordbooks.com/blog/category/kids-online-mad-libs/
from wordle import Wordle
import random
import tkinter.messagebox
from tkinter import*
import random

root = Tk()
root.geometry("650x300+0+0")
root.title("Word Games")
root.configure(background="Black")

TopsRoot = Frame(root, bg = "Black", pady = 2, width = 650, height = 100, relief = RIDGE)
TopsRoot.grid(row=0, column=0, columnspan=2)

lblTitle = Label(TopsRoot, font=('arial', 60, 'bold'), text="Word Games", bd=10, bg="Black", fg="Cornsilk", justify=CENTER)
lblTitle.grid(row=0, column=0, columnspan=3)

MainFrame = Frame(root, bg = "Grey", bd = 10, width = 650, height = 200, padx = 2, pady = 3, relief = RIDGE)
MainFrame.grid(row=1, column=0, padx = 30)




def open1():
    top = Toplevel()
    top.title("Silly Libs")
    top.geometry('500x400')  
    top.configure(background="black")
    Tops = Frame(top, bg = "Black", pady = 2, width = 1350, height = 100, relief = RIDGE)
    Tops.grid(row=0, column=0)
    lblTitle = Label(Tops, font=('arial', 30, 'bold'), text="Silly Libs Generator", bd=10, bg="Black", fg="Cornsilk", justify=CENTER)
    lblTitle.grid(row=0, column=0)
    MainFrame1 = Frame(top, bg = "Grey", bd = 10, width = 500, height = 300, padx = 2, pady = 3, relief = RIDGE)
    MainFrame1.grid(row=1, column=0, padx = 30)

    def Story1(win):  
        def final(tl: Toplevel, place1, adjective, verb1, food1, things1, profession1, thing1, color, celebrity1, animal1):   
            global text1
            text1 = f''' 
            There once was a gingerbread man who had two {things1} for eyes and a {food1} for a nose. He always said, '{verb1} as fast as you can, you can't catch me I'm the gingerbread man.' One day he ran past a {adjective} {profession1}, but they couldn't catch him. He kept running until he passed a {animal1}, but they couldn't catch him either. Suddenly, he came across a river  near {place1}. How would he cross? Then he saw a {color} {thing1} floating by. He jumped on it, but it was actually {celebrity1}--who just so happened to love cookies :)
            '''  
            tl.geometry(newGeometry='500x500')  
            tl.configure(background="Black")
            TopsStory1 = Frame(NewScreen11, bg = "Black", pady = 2, width = 500, height = 100, relief = RIDGE)
            TopsStory1.grid(row=0, column=0, columnspan=2)
            lblTitle = Label(TopsStory1, font=('arial', 30, 'bold'), text="A Gingerbread Man", bd=10, bg="Black", fg="Cornsilk", justify=CENTER)
            lblTitle.grid(row=0, column=0, columnspan=2)
            MainFrameStory1 = Frame(tl, bg = "Grey", bd = 10, width = 450, height = 400, padx = 2, pady = 3, relief = RIDGE)
            MainFrameStory1.grid(row=1, column=0, padx = 30)
            
            Label(MainFrameStory1, text='A Gingerbread Man:',  wraplength=tl.winfo_width()).place(x=150, y=0)  
            Label(MainFrameStory1, text=text1, wraplength=420, pady= 2, padx = 4,justify=CENTER).place(x=5, y=50)  
        NewScreen11 = Toplevel(win, bg='Grey')  
        NewScreen11.title("A Gingerbread Man")  
        NewScreen11.geometry('500x500')  
        NewScreen11.configure(background="Black")
        TopsStory1 = Frame(NewScreen11, bg = "Black", pady = 2, width = 500, height = 100, relief = RIDGE)
        TopsStory1.grid(row=0, column=0, columnspan=2)

        lblTitle = Label(TopsStory1, font=('arial', 30, 'bold'), text="A Gingerbread Man", bd=10, bg="Black", fg="Cornsilk", justify=CENTER)
        lblTitle.grid(row=0, column=0, columnspan=2)

        MainFrameStory1 = Frame(NewScreen11, bg = "Grey", bd = 10, width = 400, height = 400, padx = 2, pady = 3, relief = RIDGE)
        MainFrameStory1.grid(row=1, column=0, padx = 30)


        Label(MainFrameStory1, text='Place:').place(x=0, y=0)  
        Label(MainFrameStory1, text='Adjective:').place(x=0, y=35)  
        Label(MainFrameStory1, text='Verb (action):').place(x=0, y=70)  
        Label(MainFrameStory1, text='Food:').place(x=0, y=105)  
        Label(MainFrameStory1, text='Things (plural):').place(x=0, y=140)  
        Label(MainFrameStory1, text='Profession:').place(x=0, y=175)  
        Label(MainFrameStory1, text='Thing:').place(x=0, y=210) 
        Label(MainFrameStory1, text='Color:').place(x=0, y=245) 
        Label(MainFrameStory1, text='Celebrity/someone famous:').place(x=0, y=280) 
        Label(MainFrameStory1, text='Animal:').place(x=0, y=315) 
        place1 = Entry(MainFrameStory1, width=11)  
        place1.place(x=200, y=0)  
        adjective = Entry(MainFrameStory1, width=11)  
        adjective.place(x=200, y=35)  
        verb1 = Entry(MainFrameStory1, width=11)  
        verb1.place(x=200, y=70)  
        food1 = Entry(MainFrameStory1, width=11)  
        food1.place(x=200, y=105)  
        things1 = Entry(MainFrameStory1, width=11)  
        things1.place(x=200, y=140)  
        profession1 = Entry(MainFrameStory1, width=11)  
        profession1.place(x=200, y=175)  
        thing1 = Entry(MainFrameStory1, width=11)  
        thing1.place(x=200, y=210)  
        color = Entry(MainFrameStory1, width=11)  
        color.place(x=200, y=245)  
        celebrity1 = Entry(MainFrameStory1, width=11)  
        celebrity1.place(x=200, y=280)  
        animal1 = Entry(MainFrameStory1, width=11)  
        animal1.place(x=200, y=315)  
        SubmitButton1  = Button(MainFrameStory1, text="Submit", background="Grey", font=('Calibri', 12, 'bold'), command=lambda:final(NewScreen11, place1.get(), adjective.get(), verb1.get(), food1.get(), things1.get(), profession1.get(), thing1.get(), color.get(), celebrity1.get(), animal1.get(),))  
        SubmitButton1.place(x=150, y=345)  

    def Story2(win):  
        def final(tl: Toplevel, food2, profession2, adjective2, phrase, animal2, verb2, place2, celebrity2, somethingToBuy, things2):   
            global text2
            text2 = f'''
            Hi my name is {celebrity2}, but my friends call me {adjective2} {food2}. My favorite color is the color of {things2} and my favorite thing to do is {verb2}. My parents were a {animal2} and an {profession2}, which is why we lived in the {place2}. You probably know me from my TV commercial for {somethingToBuy}. I'm the one who says, '{phrase}' at the very end!
            '''  
            tl.geometry(newGeometry='500x500')  
            tl.configure(background="Black")
            TopsStory2 = Frame(NewScreen11, bg = "Black", pady = 2, width = 500, height = 100, relief = RIDGE)
            TopsStory2.grid(row=0, column=0, columnspan=2)
            lblTitle = Label(TopsStory2, font=('arial', 30, 'bold'), text="About Me", bd=10, bg="Black", fg="Cornsilk", justify=CENTER)
            lblTitle.grid(row=0, column=0, columnspan=2)
            MainFrameStory2 = Frame(tl, bg = "Grey", bd = 10, width = 450, height = 400, padx = 2, pady = 3, relief = RIDGE)
            MainFrameStory2.grid(row=1, column=0, padx = 30)
            
            Label(MainFrameStory2, text='About Me:',  wraplength=tl.winfo_width()).place(x=160, y=0)  
            Label(MainFrameStory2, text=text2, wraplength=420, pady= 2, padx = 4,justify=CENTER).place(x=5, y=50)  
        NewScreen11 = Toplevel(win, bg='Grey')  
        NewScreen11.title("About Me")  
        NewScreen11.geometry('500x500')  
        NewScreen11.configure(background="Black")
        TopsStory2 = Frame(NewScreen11, bg = "Black", pady = 2, width = 500, height = 100, relief = RIDGE)
        TopsStory2.grid(row=0, column=0, columnspan=2)

        lblTitle = Label(TopsStory2, font=('arial', 30, 'bold'), text="About Me", bd=10, bg="Black", fg="Cornsilk", justify=CENTER)
        lblTitle.grid(row=0, column=0, columnspan=2)

        MainFrameStory2 = Frame(NewScreen11, bg = "Grey", bd = 10, width = 400, height = 400, padx = 2, pady = 3, relief = RIDGE)
        MainFrameStory2.grid(row=1, column=0, padx = 30)

        Label(MainFrameStory2, text='A Food or Silly Word:').place(x=0, y=0)  
        Label(MainFrameStory2, text='Profession/Job:').place(x=0, y=35)  
        Label(MainFrameStory2, text='Adjective:').place(x=0, y=70)  
        Label(MainFrameStory2, text='Phrase/Lyrics/Saying:').place(x=0, y=105)  
        Label(MainFrameStory2, text='Animal:').place(x=0, y=140)  
        Label(MainFrameStory2, text='Verb:').place(x=0, y=175)  
        Label(MainFrameStory2, text='Place:').place(x=0, y=210) 
        Label(MainFrameStory2, text='Celebrity:').place(x=0, y=245) 
        Label(MainFrameStory2, text='Something you would buy:').place(x=0, y=280) 
        Label(MainFrameStory2, text='Things (plural):').place(x=0, y=315) 
        food2 = Entry(MainFrameStory2, width=11)  
        food2.place(x=250, y=0)  
        profession2 = Entry(MainFrameStory2, width=11)  
        profession2.place(x=250, y=35)  
        adjective2 = Entry(MainFrameStory2, width=11)  
        adjective2.place(x=250, y=70)  
        phrase = Entry(MainFrameStory2, width=11)  
        phrase.place(x=250, y=105)  
        animal2 = Entry(MainFrameStory2, width=11)  
        animal2.place(x=250, y=140)  
        verb2 = Entry(MainFrameStory2, width=11)  
        verb2.place(x=250, y=175)  
        place2 = Entry(MainFrameStory2, width=11)  
        place2.place(x=250, y=210)  
        celebrity2 = Entry(MainFrameStory2, width=11)  
        celebrity2.place(x=250, y=245)  
        somethingToBuy = Entry(MainFrameStory2, width=11)  
        somethingToBuy.place(x=250, y=280)  
        things2 = Entry(MainFrameStory2, width=11)  
        things2.place(x=250, y=315)  
        SubmitButton1  = Button(MainFrameStory2, text="Submit", background="Grey", font=('Calibri', 12), command=lambda:final(NewScreen11, food2.get(), profession2.get(), adjective2.get(), phrase.get(), animal2.get(), verb2.get(), place2.get(), celebrity2.get(), somethingToBuy.get(), things2.get(),))  
        SubmitButton1.place(x=150, y=345)  


    Story1Button = Button(MainFrame1, text='A Gingerbread Man', font=("Calibri New Roman", 16), width=30, height = 5, padx = 2, pady = 2, command=lambda: Story1(top),bg='Grey', fg="Black")  
    Story1Button.grid(row = 0, column = 0)  
    Story2Button = Button(MainFrame1, text='About Me', font=("Calibri New Roman", 16), width=30, height = 5, padx = 2, pady = 2, command=lambda: Story2(top), bg='Grey', fg="Black")  
    Story2Button.grid(row = 1, column = 0) 
    top.update()  

def open2():
    top2 = Toplevel()
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
        global test
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
        global ltrs
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
        word_set = load_word_set("wordle_words.txt")
        secret = random.choice(list(word_set))
        wordle = Wordle(secret)
        # print(secret)
        wordle.attempts = []
        lettersMatchedGreen = []
        lettersMatchedOrange = []
        assignColor()
        writeboxes()

    def clear():
        writeboxes()

    def backspace():
        global test
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
    global letters
    letters = ["QWERTYUIOP","ASDFGHJKL ","ZXCVBNM   "]

    def assignColor():
        global ltrcolor
        ltrcolor = [[] for i in range(3)]
        for i in range(3):
            for j in range(10):
                ltrcolor[i].append("LightSteelBlue1")
    global  btnNums, btnLetts,  name, newWord_, guesses, newword1, newword2, newword3, newword4, newword5, lettersPicked 

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
        global newWord_, newword1, newword2, newword3, newword4, newword5, letters, ltrcolor
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
                global btnLett_, letterKey
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

    def load_word_set(path: str):
        word_set = set()
        try:
            with open(path, "r") as f:
                for line in f.readlines():
                    word = line.strip().upper()
                    word_set.add(word)
                return word_set
        except:
            tkinter.messagebox.showinfo("Error", f"Word file wordle_words.txt Not Found!")
    global word_set, secret, wordle, result, ltrcolor, lettersMatchedGreen, lettersMatchedOrange

    word_set = load_word_set("wordle_words.txt")
    secret = random.choice(list(word_set))
    wordle = Wordle(secret)
    # print(secret)
    result = ""
    ltrcolor = []
    lettersMatchedGreen = []
    lettersMatchedOrange = []
    def checkLtrColor():
        global j, lettersMatchedGreen, lettersMatchedOrange, ltrcolor, letters, lettersPicked
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
        global lettersPicked, result
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
            clear()
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
    




def open3():
    top3 = Toplevel()
    top3.title("Hangperson")
    top3.configure(background="black")
    Tops3 = Frame(top3, bg = "Black", pady = 2, width = 500, height = 100, relief = RIDGE)
    Tops3.grid(row=0, column=0)
    lblTitle = Label(Tops3, font=('arial', 30, 'bold'), text="Hangperson", bd=10, bg="Black", fg="Cornsilk", justify=CENTER)
    lblTitle.grid(row=0, column=0)
    MainFrame1 = Frame(top3, bd = 10, width = 500, height = 400, padx = 2, pady = 3, relief = RIDGE)
    MainFrame1.grid(row=1, column=0, padx = 30)
    # computer generated
    global secret, status, hangman_art, mistakes, mistakesguesses, wrongguesses, correctguesses, level, start_button
    mistakes = 0
    wrongguesses = []
    correctguesses = []
    level = StringVar()
    status = "Start Game"

    Radiobutton(MainFrame1, text="Easy", variable = level, value = "easy_hangman_words.txt").grid(row = 0, column = 0)
    Radiobutton(MainFrame1, text="Medium", variable = level, value = "medium_hangman_words.txt").grid(row = 0, column = 1)
    Radiobutton(MainFrame1, text="Hard", variable = level, value = "all_hangman_words.txt").grid(row = 0, column = 2)

    start_button = Button(MainFrame1, text=status, bg="grey60", command = lambda: start_game(level.get()) if level.get() else tkinter.messagebox.showinfo("Error", f"Pick a level"))
    start_button.grid(row = 0, column = 4)

    def load_word_set(path: str):
        global level, word_set, word
        word_set = set()
        try:
            with open(path, "r") as f:
                for line in f.readlines():
                    word = line.strip().upper()
                    word_set.add(word)
                return word_set
        except:
            print("File not found", path, level)
    def clear():
        global hangman_label, wrongguesses_label, correctguesses_label
        wrongguesses_label.grid_forget()
        correctguesses_label.grid_forget()
        hangman_label.grid_forget()

    def start_game(level):
        
        # print(level)    
        global secret, word_list, word_set, word_with_blanks, letters_in_secret, hangman_label, status, mistakes, word_label, guess_entry, result_label, guess_button, guesses, start_button, correctguesses_label, wrongguesses_label, level_label, levelstatus
        if level == None:
            start_button.configure(state= DISABLED)
            return
        levelstatus = "Easy"
        if level == "easy_hangman_words.txt":
            levelstatus = "Easy"
        elif level == "medium_hangman_words.txt":
            levelstatus = "Medium"
        else:
            levelstatus = "Hard"
        mistakes = 0

        guesses = []
        status = "Start Game"
        wrongguesses_label = Label(MainFrame1, text=guesses, font=("Arial", 24))
        wrongguesses_label.grid(row = 4, column = 0)
        correctguesses_label = Label(MainFrame1, text=guesses, font=("Arial", 24))
        correctguesses_label.grid(row = 5, column = 0)
        start_button.configure(text = status)
        hangman_label = Label(MainFrame1, font=("Courier", 16))
        hangman_label.grid(row = 1, column = 1)
        level_label = Label(MainFrame1, text=f"Level: \n {levelstatus}", font=("Courier", 16))
        level_label.grid(row = 1, column = 3)
        word_list = level

        word_set = load_word_set(word_list)
        secret = random.choice(list(word_set)).lower()
        word_with_blanks = "_" * len(secret)
        letters_in_secret = len(secret)

        word_label = Label(MainFrame1, text=word_with_blanks, font=("Arial", 24))
        word_label.grid(row = 2, column = 1)

        letters_label = Label(MainFrame1, text=f"({letters_in_secret})", font=("Arial", 16))
        letters_label.grid(row = 2, column = 2)

        guess_button = Button(MainFrame1, text="Guess", command = lambda: check_guess(guess_entry.get()))
        guess_button.grid(row = 3, column = 2)

        guess_entry = Entry(MainFrame1, width=3, font=("Arial", 24))
        guess_entry.grid(row = 3, column = 1)

        # result_label = Label(MainFrame1, font=("Arial", 24))
        # result_label.grid(row = 4, column = 1)

        status = "New Game"
        start_button.configure(text = status)
        update_hangman(mistakes)


    #user generated TODO

    hangman_art = [
        "   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n========="
    ]

    global color
    color = "Red"
    def update_hangman(mistakes):
        global hangman_label
        hangman_label.config(text = hangman_art[mistakes])

    def check_guess(guess):
        global word_with_blanks, guesses, word_label, guess_entry, mistakes, wrongguesses_label, color, correctguesses_label
        if guess.isalpha():
            if guess in guesses:
                tkinter.messagebox.showinfo("Error", f"Already used {guess}")
                guess_entry.delete(0, END)
            else:
                if guess.lower() in secret.lower():
                    correctguesses.append(guess.lower())
                    correctguesses_label.configure(text=correctguesses, fg="Green")
                    for i in range(len(secret)):
                        if secret[i].lower() == guess.lower():
                            word_with_blanks = word_with_blanks[:i] + guess + word_with_blanks[i+1:]
                    word_label.configure(text=word_with_blanks)
                    if secret.lower() == word_with_blanks.lower():
                        end_game("win")
                    else:
                        pass
                else:
                    wrongguesses.append(guess.lower())
                    wrongguesses_label.configure(text=wrongguesses, fg="Red")
                    mistakes += 1

                    if mistakes == 6:
                        end_game("lose")
                guess_entry.delete(0, END)
                update_hangman(mistakes)
        else:
            tkinter.messagebox.showinfo("Error", f"Letter Characters Only")
            guess_entry.delete(0, END)
    def end_game(result):

        global result_label, guess_button, guess_entry, level, newgame
        if result == "win":
            result_text = "You win!. \nWould you like to play again?"
        else:
            result_text = f"You lose... the word was {secret}. \nWould you like to play again?"
        newgame = tkinter.messagebox.askquestion("Results", result_text)
        if newgame == 'yes':
            clear()
            start_game(level.get())
        else:
            top3.destroy()

btn1 = Button(MainFrame, text="Silly Libs", width=25, height = 7, padx = 2, pady = 3, command=open1).grid(row = 0, column = 0)
btn2 = Button(MainFrame, text="WordlePy", width=25, height = 7, padx = 2, pady = 3, command=open2).grid(row = 0, column = 1)
btn3 = Button(MainFrame, text="Hangperson", width=25, height = 7, padx = 2, pady = 3, command=open3).grid(row = 0, column = 2)

root.mainloop()