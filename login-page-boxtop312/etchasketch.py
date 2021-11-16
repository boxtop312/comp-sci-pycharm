from tkinter import *

window = Tk()
window.title("Etch-A-Sketch")
window.geometry("600x800")

# MODEL #
height = IntVar()
height.set(300)

# CONTROLLER #
up_down = Scale(window, from_ = 0, to = 600, label = "up & down", orient = VERTICAL, variable = height)
up_down.place(x=10,y=800,height = 200)
# VIEW #
display = Canvas(window, bg = "Teal")
display.place(x = 0, y = 0, width = 600, height = 600)

mainloop()
