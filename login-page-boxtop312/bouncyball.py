from tkinter import *
import random, math

root = Tk()
root.title("Bouncing Balls")
root.geometry("400x400")


#### DATA ####
def random_color():
	hex = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
	color ="#"
	for i in range(6):
		color+=random.choice(hex)
	print(color)
	return color




#### CONTROLLERS ####


#### VIEW ####
display = Canvas(root,bg=random_color())
display.place(x=0,y=0, width = 400, height = 400)


root.mainloop()
