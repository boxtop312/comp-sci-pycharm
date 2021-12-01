from tkinter import *
import random, math

root = Tk()
root.title("Falling Objects")
root.geometry("500x700")


#### DATA ####
# img = img.open()

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
        self.x = random.randint(10, 490)
        self.y = random.randint(10, 690)
        self.speed = 10
        self.direction = random.randint(0, 7)
        self.deltaX = self.speed * math.cos(self.direction)
        self.deltaY = self.speed * math.sin(self.direction)
        self.b = display.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius,self.y + self.radius, fill=self.color)

    def move(self, balls):
        left, top, right, bottom = self.coords()
        # Left Side of display
        if left < 0:
            self.deltaX = self.deltaX * -1
            display.move(self.b, self.deltaX + self.radius * 2, self.deltaY)
        # Right
        if right > 500:
            self.deltaX = self.deltaX * -1
            display.move(self.b, self.deltaX - self.radius * 2, self.deltaY)
        # Top
        if top < 0:
            self.deltaY = self.deltaY * -1
            display.move(self.b, self.deltaX, self.deltaY + self.radius * 2)
        # Bottom
        if bottom > 700:
            self.deltaY = self.deltaY * -1
            display.move(self.b, self.deltaX, self.deltaY - self.radius * 2)
        for b in balls:
            self.collision(b)
        display.move(self.b, self.deltaX,
                     self.deltaY)  # arguments are the object, the distance on the x axis and the distance on the y axis that we want to move the ball
        display.after(10)
        display.update()

    def collision(self, object):
        bLeft, bTop, bRight, bBottom = self.coords()
        oLeft, oTop, oRight, oBottom = object.coords()
        # Left - when ball hits the left side of the object
        if bLeft < oRight and bRight > oRight and bTop < oBottom and bBottom > oTop:
            self.deltaX = self.deltaX * -1
            display.move(self.b, self.deltaX + self.radius * 2, self.deltaY)

        # Right - when ball hits the right side of the object
        if bRight > oLeft and bLeft < oLeft and bTop < oBottom and bBottom > oTop:
            self.deltaX = self.deltaX * -1
            display.move(self.b, self.deltaX - self.radius * 2, self.deltaY)

        # Top - when ball hits the top of the object
        if bBottom > bTop and bTop < oTop and bLeft < oRight and bRight > oLeft:
            self.deltaY = self.deltaY * -1
            display.move(self.b, self.deltaX, self.deltaY + self.radius * 2)

        # Bottom - when ball hits the bottom of the object
        if bTop < oBottom and bBottom > oBottom and bRight > oLeft and bLeft < oRight:
            self.deltaY = self.deltaY * -1
            display.move(self.b, self.deltaX, self.deltaY - self.radius * 2)

    def coords(self):  # returns the coordinates for the top left corner of the object and the coordinates for the bottom right corner
        return display.coords(self.b)


class Box:
    def __init__(self):
        self.xlen = random.randint(5,25)
        self.ylen = random.randint(5,25)
        self.color = random_color()
        self.x = random.randint(10,490)
        self.y = random.randint(10,100)
        self.speed = 5
        self.direction = 3.14*2
        self.deltaX = self.speed * math.cos(self.direction)
        self.deltaY = self.speed * math.sin(self.direction)
        self.bo = display.create_rectangle(self.x - (self.xlen/2),self.y - (self.ylen/2),self.x + (self.xlen/2),self.y + (self.ylen/2),fill = self.color)

    def fall(self):
        left, top, right, bottom = self.coords()
        display.move(self.bo,0,random.randint(1,5))
        self.x = random.randint(10, 490)
        self.y = random.randint(10, 100)
        if bottom >= 700:
            display.coords(self.bo,self.x - (self.xlen/2),self.y - (self.ylen/2),self.x + (self.xlen/2),self.y + (self.ylen/2))
        display.after(10)
        display.update()

    def coords(self):  # returns the coordinates for the top left corner of the object and the coordinates for the bottom right corner
        return display.coords(self.bo)


#### CONTROLLERS ####


#### VIEW ####
display = Canvas(root, bg=random_color())
display.place(x=0, y=0, width=500, height=700)

##### CODE FOR THE GAME ######
# first = Ball()
secont = Box()

balls = []
boxes = []
for n in range(20):
    boxes.append(Box())
    # balls.append(Ball())

while True:
    # first.move(balls)
    secont.fall()
    # for ball in balls:
    #    ball.move(balls)
    for box in boxes:
        box.fall()


root.mainloop()
