from tkinter import *

root = Tk()
root.title("Canvas, Scale and Var Demo")
root.geometry("400x500")

# MODEL #
radius = IntVar()
radius.set(50)

x = 200
y = 200


def change_radius(new_intvar):
    r = radius.get()
    display.coords(circle, x-r, y-r, x+r, y+r)


# CONTROLLER #
radius_changer = Scale(root, from_ = 10, to = 200, label = "10 <-------------RADIUS-------------> 200",
orient = HORIZONTAL, variable = radius, command = change_radius)
radius_changer.place(x=50, y=425, width=300)

# VIEW #
display = Canvas(root, bg = "Teal")
display.place(x = 0, y = 0, width = 400, height = 400)

circle = display.create_oval(x-radius.get(), y-radius.get(), x+radius.get(), y+radius.get(), fill = "yellow", outline = "black")


root.mainloop()
