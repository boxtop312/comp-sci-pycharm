import random
from tkinter import*
from PIL import Image, ImageTk


root=Tk()
root.geometry("600x600")
root.title("Hangman")
# MODEL(Data and Functions) #
img1 = Image.open("1.png")
img1 = ImageTk.PhotoImage(img1)
img2 = Image.open("2.png")
img2 = ImageTk.PhotoImage(img2)
img3 = Image.open("3.png")
img3 = ImageTk.PhotoImage(img3)
img4 = Image.open("4.png")
img4 = ImageTk.PhotoImage(img4)
img5 = Image.open("5.png")
img5 = ImageTk.PhotoImage(img5)
img6 = Image.open("6.png")
img6 = ImageTk.PhotoImage(img6)
img7 = Image.open("7.png")
img7 = ImageTk.PhotoImage(img7)
words = open("words.txt","r") #opens text file for reading
wordbank = words.read() #stores contents of txt file in variable
wordbank = wordbank.split() #place words into a list.
A = random.randint(1,58110)
global Chosen_word
Chosen_word = wordbank[A]
usedlist = []
global wrong
wrong = 0
global winword
winword = ""
global game
game = 0

def dash_generator():
    global dashlist
    dashlist = []
    global generated_dashes
    for i in range(len(Chosen_word)):
        dashlist.append("_ ")
    generated_dashes = ("").join(dashlist)


dash_generator()


def sentance_checker(event):
    global Chosen_word
    global wrong
    global game
    guess = word_enter.get()
    win_checker()
    if wrong == 6:
        hangman_img.config(image = img7)
        game_set.config(text = ("You failed hangman the word was " + Chosen_word))
    elif game == 0:
        if guess not in usedlist:
            usedlist.append(str(guess))
            if guess in Chosen_word:
                for i in range(len(Chosen_word)): # checks if the guess is in the word and does the appropriate actions
                    if guess in Chosen_word[i]:
                        dashlist[i] = guess
                        generated_dashes = ("").join(dashlist)
                        word_label.config(text = generated_dashes)
                        win_checker()
                        if game == 1:
                            bg = "green"
                            game_set.config(text="you won")
            elif guess not in Chosen_word:
                wrong += 1
                incorrect_guesses.config(text = ("incorrect guesses: " + str(wrong)))
                guess_label.config(text = ", ".join(usedlist))
                if wrong == 1:
                    hangman_img.config(image = img2)
                elif wrong == 2:
                    hangman_img.config(image = img3)
                elif wrong == 3:
                    hangman_img.config(image = img4)
                elif wrong == 4:
                    hangman_img.config(image = img5)
                elif wrong == 5:
                    hangman_img.config(image = img6)


def start_game():
    dash_generator()
    hangman_img.config(image = img1)
    guess_label.config(text = "_________")
    game_set.config(text = "")
    A = random.randint(1, 58110)
    global Chosen_word
    Chosen_word = wordbank[A]
    usedlist = []
    global wrong
    wrong = 0
    global winword
    winword = ""
    global game
    game = 0
    incorrect_guesses.config(text=("incorrect guesses: " + str(wrong)))


def win_checker():
    global game
    winword = ""
    for i in range(len(dashlist)):
        winword += dashlist[i]
        if winword == Chosen_word:
            game = 1
    winword = ""


# CONTROLLER #
word_enter = Entry(root, fg = "black", font = ("Lobster 1.4",15))
word_enter.place(x = 10, y = 67, width = 200)
word_enter.bind("<Return>", sentance_checker)

stat_butt = Button(root, fg = "black", font = ("Lobster 1.4", 15), text = "start game", command = start_game)
stat_butt.place(x = 350, y = 7, width = 100)


# VIEW #
hangman_label = Label(root, fg = "black", text = "Hangman", font = ("Lobster 1.4",25))
hangman_label.place(x = 150, y = 10, width = 200)

word_label = Label(root, fg = "black", text = generated_dashes, font = ("Lobster 1.4", 15))
word_label.place(x = 250, y = 50, width = 250)

guess_label = Label(root, fg = "black", text = "_________", font = ("Lobster 1.4", 15))
guess_label.place(x = 10, y = 100, width = 300)

incorrect_guesses = Label(root, fg = "black", text = ("incorrect guesses: " + str(wrong)), font = ("Lobster 1.4", 10))
incorrect_guesses.place(x = 10, y = 123, width = 100)

game_set = Label(root, fg = "black", text = "", font = ("Lobster 1.4", 15))
game_set.place(x = 10, y = 200, width = 250)

word_enter_label = Label(root, fg = "black", text = "enter guess", font = ("lobster 1.4", 10))
word_enter_label.place(x = 10, y = 45, width = 60)

hangman_img = Label(root,image = img1)
hangman_img.place(x = 250, y = 200)

root.mainloop()
