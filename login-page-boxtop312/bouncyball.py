# from tkinter import *
# import random, math
#
# root = Tk()
# root.title("Bouncing Balls")
# root.geometry("405x405")
#
#
# # DATA #
# def random_color():
# 	hex = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
# 	color ="#"
# 	for i in range(6):
# 		color+=random.choice(hex)
# 	print(color)
# 	return color
#
#
# class Ball:
# 	# CONSTRUCTOR - responsable for making an object when it is called upon, it assings values to the attributes
# 	def __init__(self):
# 		# ATRRIBUTES - Variables that describe the state of the object being made
# 		self.radius = 10
# 		self.color = random_color()
# 		self.x = random.randint(10,390)
# 		self.y = random.randint(10,390)
# 		self.speed = random.randint(1,10)
# 		self.direction = random.randint(0,7)
# 		self.deltax = self.speed*math.cos(self.direction)
# 		self.deltay = self.speed*math.sin(self.direction)
# 		self.b = display.create_oval(self.x-self.radius,self.y-self.radius,self.x+self.radius,self.y+self.radius,fill = self.color)
# 	def move(self,balls):
# 		left,top,right,bottom = self.coords()
# 		#left side of display
# 		if left < 0:
# 			self.deltax = self.deltax*-1
# 			display.move(self.b,self.deltax + self.radius*2,self.deltay)
# 		if right > 400:
# 			self.deltax = self.deltax * -1
# 			display.move(self.b, self.deltax - self.radius * 2, self.deltay)
# 		if top < 0:
# 			self.deltay = self.deltay*-1
# 			display.move(self.b,self.deltax, self.deltay + self.radius * 2)
# 		if bottom > 400:
# 			self.deltay = self.deltay*-1
# 			display.move(self.b, self.deltax, self.deltay - self.radius * 2)
# 		for i in balls:
# 			self.colision(i)
# 		display.move(self.b,self.deltax,self.deltay)
# 		display.after(10)
# 		display.update()
# 	def coords(self):
# 		return display.coords(self.b)#returns the cordinates for the top left corner of the object and the bottom right coner
# 	def colision(self,object):
# 		bleft,btop,bright,bbottom = self.coords()
# 		oleft,otop,oright,obottom = object.coords()
# 		if bleft < oright and bright > oright and btop < obottom and bbottom > otop:
# 			self.deltax = self.deltax * -1
# 			display.move(self.b, self.deltax + self.radius * 2, self.deltay)
# 		if bright > oleft and bleft < oright and btop < obottom and bbottom > otop:
# 			self.deltax = self.deltax * -1
# 			display.move(self.b, self.deltax - self.radius * 2, self.deltay)
# 		if bbottom > otop and btop < obottom and bleft < oright and bright > oleft:
# 			self.deltay = self.deltay * -1
# 			display.move(self.b, self.deltax, self.deltay + self.radius * 2)
# 		if btop < obottom and bbottom > otop and bright > oleft and bleft < oright:
# 			self.deltay = self.deltay * -1
# 			display.move(self.b, self.deltax, self.deltay - self.radius * 2)
#
#
# # CONTROLLERS #
#
# # VIEW #
# display = Canvas(root,bg=random_color())
# display.place(x=0,y=0, width = 405, height = 405)
#
#
# # code for game#
# first = Ball()
# balls = []
# for i in range(15):
# 	balls.append(Ball())
# while True:
# 	first.move(balls)
# 	for ball in balls:
# 		ball.move(balls)
#
# root.mainloop()

import tkinter as tk
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

class Ball:
	# CONSTRUCTOR - Responsible for making an object when it is called on. It assigns values to the attributes
	def __init__(self):
		# ATTRIBUTES - variables that describe the state of the object being constructed
		self.radius = 10
		self.color = random_color()
		self.x = random.randint(10,390)
		self.y = random.randint(10,390)
		self.speed = 10
		self.direction = random.randint(0,7)
		self.deltaX = self.speed * math.cos(self.direction)
		self.deltaY = self.speed * math.sin(self.direction)
		self.b = display.create_oval(self.x - self.radius, self.y-self.radius,        self.x+self.radius, self.y+self.radius, fill = self.color)

	def move(self, balls):
		left, top, right, bottom = self.coords()
		# Left Side of display
		if left < 0 :
			self.deltaX = self.deltaX *-0.5
			display.move(self.b, self.deltaX + self.radius*2, self.deltaY)
		# Right
		if right > 400 :
			self.deltaX = self.deltaX *-0.5
			display.move(self.b, self.deltaX - self.radius*2, self.deltaY)
		# Top
		if top < 0 :
			self.deltaY = self.deltaY *-0.5
			display.move(self.b, self.deltaX, self.deltaY+ self.radius*2)
		# Bottom
		if bottom > 400 :
			self.deltaY = self.deltaY *-0.5
			display.move(self.b, self.deltaX, self.deltaY - self.radius*2)
		for b in balls:
			self.collision(b)
		display.move(self.b, self.deltaX, self.deltaY) # arguments are the object, the distance on the x axis and the distance on the y axis that we want to move the ball
		display.after(10)
		display.update()

	def collision(self, object):
		bLeft, bTop, bRight, bBottom = self.coords()
		oLeft, oTop, oRight, oBottom = object.coords()
		# Left - when ball hits the left side of the object
		if bLeft < oRight and bRight > oRight and bTop < oBottom and bBottom > oTop:
			self.deltaX = self.deltaX *-0.5
			display.move(self.b, self.deltaX + self.radius*2, self.deltaY)

		# Right - when ball hits the right side of the object
		if bRight > oLeft and bLeft < oLeft and bTop < oBottom and bBottom > oTop:
			self.deltaX = self.deltaX *-0.5
			display.move(self.b, self.deltaX - self.radius*2, self.deltaY)

		# Top - when ball hits the top of the object
		if bBottom > oTop and bTop < oTop and bLeft < oRight and bRight > oLeft:
			self.deltaY = self.deltaY *-0.5
			display.move(self.b, self.deltaX, self.deltaY+ self.radius*2)

		# Bottom - when ball hits the bottom of the object
		if bTop < oBottom and bBottom > oBottom and bRight > oLeft and bLeft < oRight:
			self.deltaY = self.deltaY *-0.5
			display.move(self.b, self.deltaX, self.deltaY - self.radius*2)




	def coords(self): # returns the coordinates for the top left corner of the object and the coordinates for the bottom right corner
		return display.coords(self.b)


#### CONTROLLERS ####


#### VIEW ####
display = Canvas(root,bg=random_color())
display.place(x=0,y=0, width = 400, height = 400)



##### CODE FOR THE GAME ######
first  = Ball()

balls = []
for n in range(15):
	balls.append(Ball())

while True:
	first.move(balls)
	for ball in balls:
		ball.move(balls)





root.mainloop()
