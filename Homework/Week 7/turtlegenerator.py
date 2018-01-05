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

# function to reset and clear the screen
def reset_screen():
    screen.reset()
    pen.speed(0)
    pen.color('blue')
    pen.width(3)
    
# button widgets

def clearF():
    # clear the entry-s
    orderStr.set("")
    lengthStr.set("")
    reset_screen()
    return


clearButton = Button(root, text = "Clear", command = clearF)
clearButton.grid(row = 3, column = 1)
    
def draw():
    items = listbox.curselection()
    
    selected_item = items[0]
    
    order  = int(orderStr.get())
    length = float(lengthStr.get())
    
    if selected_item == figures.index("Tree"):
        turtlegraphics.tree(order, length, pen)
        
    elif selected_item == figures.index("Gasket"):
        turtlegraphics.gasket(order, length, pen)
        
    elif selected_item == figures.index("Koch"):
        turtlegraphics.k(order, length, pen)
    
    elif selected_item == figures.index("Tree4"):
        turtlegraphics.tree4(order, length, pen)
        
    elif selected_item == figures.index("Flake"):
        turtlegraphics.flake(order, length, pen)
        
    return


drawButton = Button(root, text="Draw", command=draw)
drawButton.grid(column=3, row=3)

# list widget

listbox = Listbox(root)
listbox.grid(row=1, column=3, rowspan = 2)

figures = ["Tree", "Gasket", "Koch", "Tree4", "Flake"]

for figure in figures:
    listbox.insert(END, figure)

# make a screen and a pen
pen = Pen()
screen = Screen()

pen.speed(0)
pen.color('blue')
pen.width(3)

screen.bgcolor('red')

root.mainloop()













