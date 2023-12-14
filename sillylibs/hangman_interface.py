from tkinter import *   
import tkinter.messagebox
import random

top3 = Tk()
top3.title("Hangman")

# computer generated
global secret, status, hangman_art, mistakes, mistakesguesses, wrongguesses, correctguesses, level
mistakes = 0
wrongguesses = []
correctguesses = []
level = StringVar()
status = "Start Game"

Radiobutton(top3, text="Easy", variable = level, value = "easy_hangman_words.txt").grid(row = 0, column = 0)
Radiobutton(top3, text="Medium", variable = level, value = "medium_hangman_words.txt").grid(row = 0, column = 1)
Radiobutton(top3, text="Hard", variable = level, value = "all_hangman_words.txt").grid(row = 0, column = 2)

start_button = Button(top3, text=status, command = lambda: start_game(level.get()))
start_button.grid(row = 0, column = 4)

def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
        return word_set
    
def clear():
    global hangman_label, guesses_label
    guesses_label.grid_forget()
    hangman_label.grid_forget()

def start_game(level = "easy_hangman_words.txt"):
    global secret, word_list, word_set, word_with_blanks, letters_in_secret, hangman_label, status, mistakes, word_label, guess_entry, result_label, guess_button, guesses, start_button, correctguesses_label, wrongguesses_label, level_label, levelstatus
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
    wrongguesses_label = Label(top3, text=guesses, font=("Arial", 24))
    wrongguesses_label.grid(row = 4, column = 0)
    correctguesses_label = Label(top3, text=guesses, font=("Arial", 24))
    correctguesses_label.grid(row = 5, column = 0)
    start_button.configure(text = status)
    hangman_label = Label(top3, font=("Courier", 16))
    hangman_label.grid(row = 1, column = 1)
    level_label = Label(top3, text=f"Level: \n {levelstatus}", font=("Courier", 16))
    level_label.grid(row = 1, column = 3)
    word_list = level

    word_set = load_word_set(word_list)
    secret = random.choice(list(word_set)).lower()
    word_with_blanks = "_" * len(secret)
    letters_in_secret = len(secret)

    word_label = Label(top3, text=word_with_blanks, font=("Arial", 24))
    word_label.grid(row = 2, column = 1)

    letters_label = Label(top3, text=f"({letters_in_secret})", font=("Arial", 16))
    letters_label.grid(row = 2, column = 2)

    guess_button = Button(top3, text="Guess", command = lambda: check_guess(guess_entry.get()))
    guess_button.grid(row = 3, column = 2)

    guess_entry = Entry(top3, width=3, font=("Arial", 24))
    guess_entry.grid(row = 3, column = 1)

    # result_label = Label(top3, font=("Arial", 24))
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
                print(mistakes)
                if mistakes == 6:
                    end_game("lose")
            guess_entry.delete(0, END)
            update_hangman(mistakes)
    else:
        tkinter.messagebox.showinfo("Error", f"Letter Characters Only")
        guess_entry.delete(0, END)
def end_game(result):
    print(result)
    global result_label, guess_button, guess_entry, level, newgame
    if result == "win":
        result_text = "You win!. \nWould you like to play again?"
    else:
        result_text = f"You lose... the word was {secret}. \nWould you like to play again?"
    newgame = tkinter.messagebox.askquestion("Results", result_text)
    if newgame == 'yes':
        clear()
        start_game()
    else:
        top3.destroy()

top3.mainloop()