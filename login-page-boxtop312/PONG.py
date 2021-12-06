from tkinter import *

root = Tk()
root.title("PONG")
# MODEL (Data) #
game = Frame(root,bg = "teal")
game.place(x=0,y=0,width = 400,height=400)
start = Frame(root,bg = "Black")
start.place(x=0,y=0,width = 400,height=400)


def start_game(event):
    game.tkraise()


# CONTROLLERS #
game = Button(start,text = "Press to start", bg = "black",fg = "white", command = start_game,font = ("Lobster 1.4"))
game.place(x=200,y=200)
# VIEW #


root.mainloop()
