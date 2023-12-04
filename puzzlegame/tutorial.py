from tkinter import *

root = Tk()
root.title("Simple Calculator")
e = Entry(root, width=30, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

total = None

def button_click(num):
    current = str(e.get()) + str(num)
    e.delete(0, END)
    e.insert(0, current)

    
def button_clear():
    e.delete(0, END)
    global total
    total = None

def button_add():
    global total
    global math
    math = "addition"
    if total == None:
        total = 0
    total += int(e.get())
    e.delete(0, END)

def button_subtract():
    global total
    global math
    math = "subtraction"
    if total == None:
        total = int(e.get())
    else:    
        total -= int(e.get())
    e.delete(0, END)

def button_multiply():
    global total
    global math
    math = "multiplication"
    if total == None:
        total = 1
        total = total * int(e.get())
    else:
        total = total * int(e.get())
    e.delete(0, END)

def button_divide():
    global total
    global math
    math = "division"
    if total == None:
        total = int(e.get())

    else:
        total = total / int(e.get())
    e.delete(0, END)



def button_equal():
    global total 
    global math
    if total == None:
        pass
    else:
        if math == "addition":
            total += int(e.get())
        elif math == "subtraction":
            total -= int(e.get())
        elif math == "multiplication":
            total = total * int(e.get())
        elif math == "division":
            if int(e.get()) == 0:
                e.insert(0, "ERR")
                return
            else:
                total = total / int(e.get())
        e.delete(0, END)
        e.insert(0, total)
    total = None

# define buttons

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)
button_subtract = Button(root, text="-", padx=42, pady=20, command=button_subtract)
button_multiply= Button(root, text="*", padx=43, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=42, pady=20, command=button_divide)


# Put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_add.grid(row=6, column=0)
button_equal.grid(row=6, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)
button_subtract.grid(row=5, column=0)
button_multiply.grid(row=5, column=1)
button_divide.grid(row=5, column=2)


root.mainloop()