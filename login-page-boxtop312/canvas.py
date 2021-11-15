from tkinter import *

root = Tk()
root.title("Canvas, Scale and Var Demo")
root.geometry("400x500")

#### MODEL ####


#### CONTROLLER ####
radius_changer = Scale(root)

#### VIEW ####
display = Canvas(root, bg = "Teal")
display.place(x = 0, y = 0, width = 400, height = 400)


root.mainloop()