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


def start_game():
    game.tkraise()


def random_color():
    hex = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    color = "#"
    for i in range(6):
        color += random.choice(hex)
    print(color)
    return color


class Ball:
    # CONSTRUCTOR - Responsible for making an object when it is called on. It assigns values to the attributes
    def __init__(self):
        # ATTRIBUTES - variables that describe the state of the object being constructed
        self.radius = 10
        self.color = random_color()
        self.x = random.randint(10, 390)
        self.y = random.randint(10, 390)
        self.speed = 10
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
        # Right
        if right > 400:
            self.deltaX = self.deltaX * -0.5
            display.move(self.b, self.deltaX - self.radius * 2, self.deltaY)
        # Top
        if top < 0:
            self.deltaY = self.deltaY * -0.5
            display.move(self.b, self.deltaX, self.deltaY + self.radius * 2)
        # Bottom
        if bottom > 400:
            self.deltaY = self.deltaY * -0.5
            display.move(self.b, self.deltaX, self.deltaY - self.radius * 2)
        for b in balls:
            self.collision(b)
        display.move(self.b, self.deltaX,self.deltaY)  # arguments are the object, the distance on the x axis and the distance on the y axis that we want to move the ball
        display.after(10)
        display.update()

    def collision(self, object):
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


# CONTROLLERS #
startbutt = Button(start, text="Press to start", bg="black", fg="white", command=start_game, font=("Lobster 1.4", 10))
startbutt.place(x=150, y=450)

ballsizeenter = Entry(start,font = ("Lobster 1.4",15),bg = "black",fg = "white")
ballsizeenter.place(x = 95,y = 10)
ballspeedenter = Entry(start,font = ("Lobster 1.4",15),bg = "black",fg = "white")
ballspeedenter.place(x = 106,y = 45)
paddlesizeenter = Entry(start,font = ("Lobster 1.4",15), bg = "black",fg = "white")
paddlesizeenter.place(x = 115,y = 80)
# VIEW #
Logo = Label(start,font = ("Lobster 1.4",50),bg = "black", fg ="White",text = "Not 'pong'")
Logo.place(x = 60,y = 200)
ballsizelabel = Label(start,font = ("Lobster 1.4",15),bg = "black",fg = "white",text = "Ball Size:")
ballsizelabel.place(x = 10,y = 10)
ballspeedlable = Label(start,font = ("Lobster 1.4",15),bg = "black",fg = "white",text = "Ball Speed:")
ballspeedlable.place(x = 10,y =45)
paddlesizelabel = Label(start,font = ("Lobster 1.4",15),bg = "black",fg = "White",text = "Paddle Size:")
paddlesizelabel.place(x=10,y = 80)

display = Canvas(game, bg="teal")
display.place(x=0, y=0, width=400, height=400)

first = Ball()
balls = []
while True:
    first.move(balls)

root.mainloop()

