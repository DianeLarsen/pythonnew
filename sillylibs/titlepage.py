#Source for madlibs: https://www.glowwordbooks.com/blog/category/kids-online-mad-libs/

import random
import tkinter.messagebox
from tkinter import*

root = Tk()
root.geometry("800x300+0+0")
root.title("Word Games")
root.configure(background="Black")

TopsRoot = Frame(root, bg = "Black", pady = 2, width = 800, height = 100, relief = RIDGE)
TopsRoot.grid(row=0, column=0, columnspan=2)

lblTitle = Label(TopsRoot, font=('arial', 60, 'bold'), text="Word Games", bd=10, bg="Black", fg="Cornsilk", justify=CENTER)
lblTitle.grid(row=0, column=0, columnspan=3)

MainFrame = Frame(root, bg = "Grey", bd = 10, width = 800, height = 200, padx = 2, pady = 3, relief = RIDGE)
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
    top2.geometry('500x400')  
    top2.configure(background="black")
    Tops2 = Frame(top2, bg = "Black", pady = 2, width = 1350, height = 100, relief = RIDGE)
    Tops2.grid(row=0, column=0)
    lblTitle = Label(Tops2, font=('arial', 30, 'bold'), text="Silly Libs Generator", bd=10, bg="Black", fg="Cornsilk", justify=CENTER)
    lblTitle.grid(row=0, column=0)
    MainFrame1 = Frame(top2, bg = "Grey", bd = 10, width = 500, height = 300, padx = 2, pady = 3, relief = RIDGE)
    MainFrame1.grid(row=1, column=0, padx = 30)
    




def open3():
    top3 = Toplevel()
    top3.title("Hangman")
    top3.configure(background="Black")
    top3.geometry('500x400')  
    top3.configure(background="black")
    Tops3 = Frame(top3, bg = "Black", pady = 2, width = 1350, height = 100, relief = RIDGE)
    Tops3.grid(row=0, column=0)
    lblTitle = Label(Tops3, font=('arial', 30, 'bold'), text="Silly Libs Generator", bd=10, bg="Black", fg="Cornsilk", justify=CENTER)
    lblTitle.grid(row=0, column=0)
    MainFrame1 = Frame(top3, bg = "Grey", bd = 10, width = 500, height = 300, padx = 2, pady = 3, relief = RIDGE)
    MainFrame1.grid(row=1, column=0, padx = 30)

btn1 = Button(MainFrame, text="Silly Libs", width=25, height = 7, padx = 2, pady = 3, command=open1).grid(row = 0, column = 0)
btn2 = Button(MainFrame, text="WordlePy", width=25, height = 7, padx = 2, pady = 3, command=open2).grid(row = 0, column = 1)
btn3 = Button(MainFrame, text="Hangman", width=25, height = 7, padx = 2, pady = 3, command=open3).grid(row = 0, column = 2)

root.mainloop()