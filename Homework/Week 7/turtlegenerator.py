'''
program for euro to dollar convertion using the rate = 1.23
'''

from tkinter import *
import turtlegraphics
from turtle import *
import math


# setup the window
root = Tk()
root.title("Turtle Fractals Generator")
root.geometry("300x200+100+100")

# make the interface
turtleLabel = Label(root, text = "Turtle Fractals Generator")
turtleLabel.grid(row = 0, column = 1, columnspan = 2)

# order widgets
orderLabel = Label(root, text = "Order")
orderLabel.grid(row = 1, column =0)

orderStr = StringVar()
orderEntry = Entry(root, textvariable = orderStr)
orderEntry.grid(row = 1, column =1, columnspan = 2)

#length widgets
lengthLabel = Label(root, text = "Length")
lengthLabel.grid(row = 2, column =0)

lengthStr = StringVar()
lengthEntry = Entry(root, textvariable = lengthStr)
lengthEntry.grid(row = 2, column =1, columnspan = 2)

# button widgets

def clearF():
    # clear the entry-s
    orderStr.set("")
    lengthStr.set("")
    
    return


clearButton = Button(root, text = "Clear", command = clearF)
clearButton.grid(row = 3, column = 1)

def treeF():
    order  = int(orderStr.get())
    length = float(lengthStr.get())
    turtlegraphics.tree(order, length, pen)
    
    return

treeButton = Button(root, text = "Tree", command = treeF)
treeButton.grid(row = 1, column = 3)

def gasketF():
	order = int(orderStr.get())
	length = float(lengthStr.get())
	
	turtlegraphics.gasket(order, length, pen)
	
	return
	
gasketButton = Button(root, text="Gasket", command = gasketF)
gasketButton.grid(row=2, column=3)

def kochF():
	order = int(orderStr.get())
	length = float(lengthStr.get())
	
	turtlegraphics.k(order, length, pen)
	
	return
	
kochButton = Button(root, text="Koch", command=kochF)
kochButton.grid(row=3, column=3)

def tree4F():
	order = int(orderStr.get())
	length = float(lengthStr.get())
	
	turtlegraphics.tree4(order, length, pen)
	
	return

tree4Button = Button(root, text="Tree 4", command=tree4F)
tree4Button.grid(row=4, column=3)

def flakeF():
	order = int(orderStr.get())
	length = float(lengthStr.get())
	
	turtlegraphics.flake(order, length, pen)
	
	return

flakeButton = Button(root, text="Flake", command=tree4F)
flakeButton.grid(row=5, column=3)

# make a screen and a pen
pen = Pen()
screen = Screen()

pen.speed(0)
pen.color('blue')
pen.width(3)

screen.bgcolor('red')

root.mainloop()













