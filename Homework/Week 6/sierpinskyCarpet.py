'''
program to draw turtle fractals
'''

from turtle import *
import math

# Make a screen and a pen
pen = Pen()
screen = Screen()

pen.speed(100)
pen.color("blue")
pen.width(0)

screen.bgcolor("red")

def sierpinskyCurve(n, l):
	
	# Termination
	if n == 0 or n == 1:
		return
		
	d = l/2
	
	sierpinskyCurve(n-1, l)
	pen.right(45); pen.forward(d); pen.right(45)
	
	sierpinskyCurve(n-1, l)
	pen.left(90); pen.forward(l); pen.left(90)
	
	sierpinskyCurve(n-1, l)
	pen.right(45); pen.forward(d); pen.right(45)
	
	sierpinskyCurve(n-1, l)
	
def sierpinskyCarpet(n, l):
	
	sierpinskyCurve(n, l)
	
	pen.left(90)
	sierpinskyCarpet(n, l)
	
	pen.left(90)
	sierpinskyCarpet(n, l)
	
	pen.left(90)
	sierpinskyCarpet(n, l)
	
	
	
sierpinskyCarpet(4, 12)
