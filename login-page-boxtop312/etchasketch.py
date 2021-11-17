from tkinter import *

window = Tk()
window.title("Etch-A-Sketch")
window.geometry("600x800")

# MODEL #
global oldY
oldY = 300
global oldX
oldX = 300
global color
color = "black"

newY = IntVar()
newY.set(300)

newX = IntVar()
newX.set(300)


def draw_line(IntVar):
    global color,oldX,oldY
    display.create_line(oldX,oldY,newX.get(),newY.get(),fill = color, width = 1)
    oldX = newX.get()
    oldY = newY.get()



def colorchanger(color1):
    global color
    color = color1


def clearscreen():
    display.delete(ALL)


# CONTROLLER #
up_down = Scale(window, from_ = 0, to = 600,font = ("Lobster 1.4",10), orient = VERTICAL, variable = newY, command = draw_line)
up_down.place(x=10,y=598,height = 200)

up_down_label = Label(window, text = "u\np\n \n&\n \nd\no\nw\nn\n", font = ("Lobster 1.4",10))
up_down_label.place(x = 53, y = 600)

left_right = Scale(window, from_ = 0, to = 600,font = ("Lobster 1.4",10),label = "left & right", orient = HORIZONTAL, variable = newX, command = draw_line)
left_right.place(x = 200, y = 600, width = 200)

blackbutt = Button(window, fg = "white", bg = "black",font = ("Lobster1.4",15), text = "Black", command = lambda :colorchanger("Black"))
blackbutt.place(x = 200, y = 700, width = 75, height = 20)

whitebutt = Button(window, fg = "black", bg = "white", font = ("Lobster 1.4",15),text = "White", command = lambda :colorchanger("White"))
whitebutt.place(x = 200,y = 720,width = 75,height = 20)

redbutt = Button(window, fg = "black", bg = "Red", font = ("Lobster 1.4",15), text = "Red", command = lambda :colorchanger("Red"))
redbutt.place(x = 275,y = 700,width = 75,height = 20)

orangebutt = Button(window, fg = "black", bg = "Orange", font = ("Lobster 1.4",15), text = "Orange", command = lambda :colorchanger("Orange"))
orangebutt.place(x = 350,y = 700,width = 75, height = 20)

yellowbutt = Button(window, fg = "black", bg = "Yellow", font = ("Lobster 1.4",15),text = "Yellow", command = lambda :colorchanger("Yellow"))
yellowbutt.place(x = 275,y = 720,width = 75,height = 20)

greenbutt = Button(window, fg = "black", bg = "green", font = ("Lobster 1.4",15),text = "Green", command = lambda :colorchanger("Green"))
greenbutt.place(x = 350,y = 720,width = 75,height = 20)

bluebutt = Button(window,fg = "black", bg = "blue", font = ("Lobster 1.4",15),text = "Blue", command = lambda :colorchanger("Blue"))
bluebutt.place(x = 200,y = 740,width = 75,height = 20)

purplebutt = Button(window,fg = "Black", bg = "purple", font = ("Lobster 1.4",15), text = "Purple", command = lambda :colorchanger("Purple"))
purplebutt.place(x = 350,y = 740,width = 75,height = 20)

clearbutt = Button(window,fg = "black", font = ("Lobster 1.4",15),text = "Clear", command = clearscreen)
clearbutt.place(x = 275,y = 740,width = 75,height =20)

# VIEW #
display = Canvas(window, bg = "teal")
display.place(x = 0, y = 0, width = 600, height = 600)

mainloop()
