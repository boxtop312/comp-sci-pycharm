from tkinter import *
import random, math

root = Tk()
root.title("PONG")
root.geometry("400x500")
# MODEL (Data) #
game = Frame(root, bg="teal")
game.place(x=0, y=0, width=400, height=500)
start = Frame(root, bg="Black")
start.place(x=0, y=0, width=400, height=500)
slider1 = IntVar()
slider1.set(0)
slider2 = IntVar()
slider2.set(0)
slider3 = IntVar()
slider3.set(0)
name1 = StringVar()
name2 = StringVar()
score1 = IntVar()
score1.set(0)
score2 = IntVar()
score2.set(0)


def start_game():
    name1.set(name1enter.get())
    player1label.config(text = (name1.get() + " \nScore: "+str(score1.get())))
    name2.set(name2enter.get())
    player2label.config(text = (name2.get()+"\nScore: "+str(score2.get())))
    game.tkraise()
    move_ball()


def random_color():
    hex = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    color = "#"
    for i in range(6):
        color += random.choice(hex)
    print(color)
    return color


def move_ball():
    global paddels
    first = Ball()
    secont = Paddle("<w>","<s>")
    third = Paddle("<Up>","<Down>")
    balls = []
    paddels = []
    paddels.append(secont)
    paddels.append(third)
    while True:
        first.move(balls)
        secont.move()
        third.move()

class Ball:
    # CONSTRUCTOR - Responsible for making an object when it is called on. It assigns values to the attributes
    def __init__(self):
        # ATTRIBUTES - variables that describe the state of the object being constructed
        self.radius = slider1.get()/2
        self.color = random_color()
        self.x = random.randint(10, 390)
        self.y = random.randint(10, 390)
        self.speed = slider2.get()
        self.direction = random.randint(0, 7)
        self.deltaX = self.speed * math.cos(self.direction)
        self.deltaY = self.speed * math.sin(self.direction)
        self.b = display.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius,self.y + self.radius, fill=self.color)

    def move(self, balls):
        left, top, right, bottom = self.coords()
        # Left Side of display
        if left < 0:
            self.deltaX = self.deltaX * -0.5
            display.move(self.b, self.deltaX + self.radius * 2, self.deltaY)
            score2.set(+1)
            player2label.config(text=(name2.get() + "\nScore: " + str(score2.get())))
        # Right
        if right > 400:
            self.deltaX = self.deltaX * -0.5
            display.move(self.b, self.deltaX - self.radius * 2, self.deltaY)
            score1.set(+1)
            player1label.config(text=(name1.get() + " \nScore: " + str(score1.get())))
        # Top
        if top < 0:
            self.deltaY = self.deltaY * -0.5
            display.move(self.b, self.deltaX, self.deltaY + self.radius * 2)
        # Bottom
        if bottom > 400:
            self.deltaY = self.deltaY * -0.5
            display.move(self.b, self.deltaX, self.deltaY - self.radius * 2)
        for p in paddels:
            self.collision(p)
        display.move(self.b, self.deltaX,self.deltaY)  # arguments are the object, the distance on the x axis and the distance on the y axis that we want to move the ball
        display.after(10)
        display.update()

    def collision(self, object):
        # self.speed = slider2.get()
        # self.deltaX = math.acos(int(self.deltaX/self.speed))
        # self.deltaY = math.asin(int(self.deltaY/self.speed))
        bLeft, bTop, bRight, bBottom = self.coords()
        oLeft, oTop, oRight, oBottom = object.coords()
        # Left - when ball hits the left side of the object
        if bLeft < oRight and bRight > oRight and bTop < oBottom and bBottom > oTop:
            self.deltaX = self.deltaX * -0.5
            display.move(self.b, self.deltaX + self.radius * 2, self.deltaY)

        # Right - when ball hits the right side of the object
        if bRight > oLeft and bLeft < oLeft and bTop < oBottom and bBottom > oTop:
            self.deltaX = self.deltaX * -0.5
            display.move(self.b, self.deltaX - self.radius * 2, self.deltaY)

        # Top - when ball hits the top of the object
        if bBottom > oTop and bTop < oTop and bLeft < oRight and bRight > oLeft:
            self.deltaY = self.deltaY * -0.5
            display.move(self.b, self.deltaX, self.deltaY + self.radius * 2)

        # Bottom - when ball hits the bottom of the object
        if bTop < oBottom and bBottom > oBottom and bRight > oLeft and bLeft < oRight:
            self.deltaY = self.deltaY * -0.5
            display.move(self.b, self.deltaX, self.deltaY - self.radius * 2)

    def coords(self):  # returns the coordinates for the top left corner of the object and the coordinates for the bottom right corner
        return display.coords(self.b)




class Paddle:
    # CONSTRUCTOR - Responsible for making an object when it is called on. It assigns values to the attributes
    def __init__(self,up,down):
        # ATTRIBUTES - variables that describe the state of the object being constructed
        self.length = slider3.get()
        self.color = random_color()
        placelist = [11,389]
        self.x = random.choice(placelist)
        self.y = 200
        self.speed = 10
        self.direction = 0
        self.deltaX = self.speed * math.cos(self.direction)
        self.deltaY = self.speed * math.sin(self.direction)
        root.bind(up, self.up)
        root.bind(down, self.down)
        self.p = display.create_rectangle(self.x-2.5,self.y-self.length,self.x+2.5,self.y+self.length,fill = self.color)

    def move(self):
        left, top, right, bottom = self.coords()
        if top < 0:
            display.move(self.p, 0, self.length + 10)
        if bottom > 400:
            display.move(self.p, 0, (self.length * -1) - 5)
        display.after(10)
        display.update()


    def up(self,event):
        self.direction = 3.14 * 2
        self.deltaY = self.speed * math.sin(self.direction)
        display.move(self.p, 0, -10)
        self.move()


    def down(self,event):
        self.direction = 3.14 / 2
        self.deltaY = self.speed * math.sin(self.direction)
        display.move(self.p, 0, self.deltaY)
        self.move()

    def coords(self):  # returns the coordinates for the top left corner of the object and the coordinates for the bottom right corner
        return display.coords(self.p)


# CONTROLLERS #
startbutt = Button(start, text="Press to start", bg="black", fg="white", command=start_game, font=("Lobster 1.4", 10))
startbutt.place(x=150, y=450)

ballsizeenter = Scale(start,font = ("Lobster 1.4",10),bg = "black",fg = "white",orient = "horizontal",from_ = 2,to = 40,variable = slider1)
ballsizeenter.place(x = 95,y = 5,height = 40,width = 250)
ballspeedenter = Scale(start,font = ("Lobster 1.4",10),bg = "black",fg = "white",orient = "horizontal",from_ = 2,to = 20,variable = slider2)
ballspeedenter.place(x = 106,y = 52,height = 40,width = 250)
paddlesizeenter = Scale(start,font = ("Lobster 1.4",10), bg = "black",fg = "white",orient = "horizontal",from_ = 1,to = 50,variable = slider3)
paddlesizeenter.place(x = 115,y = 98,height = 40,width = 250)

name1enter = Entry(start,font = ("Lobster 1.4",15),bg = "Black",fg = "white")
name1enter.place(x = 130,y = 300)
name2enter = Entry(start,font = ("Lobster 1.4",15),bg = "black",fg = "white")
name2enter.place(x = 130,y = 350)
# VIEW #
Logo = Label(start,font = ("Lobster 1.4",50),bg = "black", fg ="White",text = "Not 'pong'")
Logo.place(x = 60,y = 200)
ballsizelabel = Label(start,font = ("Lobster 1.4",15),bg = "black",fg = "white",text = "Ball Size:")
ballsizelabel.place(x = 10,y = 10)
ballspeedlable = Label(start,font = ("Lobster 1.4",15),bg = "black",fg = "white",text = "Ball Speed:")
ballspeedlable.place(x = 10,y =52)
paddlesizelabel = Label(start,font = ("Lobster 1.4",15),bg = "black",fg = "White",text = "Paddle Size:")
paddlesizelabel.place(x=10,y = 98)
player1namelabel = Label(start,font = ("Lobster 1.4",15),bg = "Black",fg = "white",text = "player1 name:")
player1namelabel.place(x = 10,y = 300)
player2namelabel = Label(start,font = ("Lobster 1.4",15),bg = "Black",fg = "white",text = "player2 name:")
player2namelabel.place(x = 10,y = 350)

player1label = Label(game,font = ("Lobster 1.4",10), bg = "teal",fg = "Black",text = "")
player1label.place(x=10,y=410)
player2label = Label(game,font = ("Lobster 1.4",10),bg = "teal",fg = "black",text = "")
player2label.place(x = 320,y = 410)

display = Canvas(game, bg="teal")
display.place(x=0, y=0, width=400, height=400)


root.mainloop()
