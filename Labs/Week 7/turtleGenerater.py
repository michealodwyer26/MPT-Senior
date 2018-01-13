'''
program for euro to dollar conversion using the rate = 1.23
'''

from tkinter import *
import turtleGraphics
from turtle import *
import math

# Make a screen and a pen
pen = Pen()
screen = Screen()

pen.speed(0)
pen.color("blue")
pen.width(3)

screen.bgcolor("red")

# Set up the window
root = Tk()
root.title("Turtle Generator")
root.geometry("300x200+100+100")

# make the interface
turtleLabel = Label(root, text="Turtle Fractals Generator")
turtleLabel.grid(row=0, column=1, columnspan=2)

# order widgets
orderLabel = Label(root, text="Order")
orderLabel.grid(row=1, column=0)

orderStr = StringVar()
orderEntry = Entry(root, textvariable= orderStr)
orderEntry.grid(row=1, column=1, columnspan=2)

# length widgets
lengthLabel = Label(root, text="Length")
lengthLabel.grid(row=2, column=0)

lengthStr = StringVar()
lengthEntry = Entry(root, textvariable= lengthStr)
lengthEntry.grid(row=2, column=1, columnspan=2)

def clearF():
	# clear the entrys
	orderStr.set("4")
	lengthStr.set("200")
	return

clearButton = Button(root, text="Clear", command=clearF)
clearButton.grid(row=3, column=1)

def treeF():
	order = float(orderStr.get())
	length = float(lengthStr.get())
	
	turtleGraphics.tree(order, length, pen)
	
	return
	

treeButton = Button(root, text="Tree", command=treeF)
treeButton.grid(row=1, column=3)

root.mainloop()