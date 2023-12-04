from tkinter import *
from PIL import Image
from PIL import ImageTk
root = Tk()
root.title("Images")

image = Image.open('puzzleicon.ico')
image = image.resize((16, 16))


root.iconbitmap("puzzleicon.ico")

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()


root.mainloop()