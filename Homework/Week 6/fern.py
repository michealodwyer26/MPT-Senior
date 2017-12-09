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
pen.width(3)

screen.bgcolor("red")

def fern(n, l):
	# Termination
	if n == 0:
		return
		
	pen.forward(0.3*l)
	
	pen.left(55)
	fern(n-1, l/2)
	pen.right(55)
	
	pen.forward(0.7*l)
	
	pen.right(40)
	fern(n-1, l/2)
	pen.left(40)
	
	pen.forward(l)
	
	pen.left(5)
	fern(n-1, 0.8*l)
	pen.right(5)
	
	pen.backward(2*l)
	
fern(8, 200)
	
	
	