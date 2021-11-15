from tkinter import *

root = Tk()
root.title("Canvas, Scale and Var Demo")
root.geometry("400x500")

#### MODEL ####


#### CONTROLLER ####
radius_changer = Scale(root, from_ = 10, to = 200, label = "10 <-------------RADIUS--------------> 200", orient = HORIZONTAL)
radius_changer.place(x=50,y=425,width=300)

#### VIEW ####
display = Canvas(root, bg = "Teal")
display.place(x = 0, y = 0, width = 400, height = 400)

circle = display.create_oval()

root.mainloop()
