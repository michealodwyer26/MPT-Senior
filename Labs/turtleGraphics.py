'''
program to draw turtle fractals
'''
from turtle import *
import math

# Make a screen and a pen
pen = Pen()
screen = Screen()

pen.speed(0)
pen.color("blue")
pen.width(3)

screen.bgcolor("red")
def gasket(n, l):
	# termination
	if n == 0 or l<2:
		pen.forward(l); pen.left(120)
		pen.forward(l); pen.left(120)
		pen.forward(l); pen.left(120)
		return
		
	gasket(n-1, l/2); pen.forward(l); pen.left(120)
	gasket(n-1, l/2); pen.forward(l); pen.left(120)
	gasket(n-1, l/2); pen.forward(l); pen.left(120)

def tree(n, l, pen):
	# Terminatiom
	if n == 0 or l < 2:
		return 
		
	pen.forward(l)
	pen.left(45)
	tree(n-1, l/2, pen)
	pen.right(90)
	tree(n-1, l/2, pen)
	pen.left(45)
	pen.backward(l)
	
def tree4(n, l):
	# Termination
	if n == 0 or l < 2:
		return
		
	pen.forward(l)
	
	pen.left(90)
	
	tree4(n-1, l/2)
	pen.right(60)
	
	tree4(n-1, l/2)
	pen.right(60)
	
	tree4(n-1, l/2)
	pen.right(60)
	
	tree4(n-1, l/2)
	
	pen.left(90)
	
	pen.backward(l)
	
def k(n, l):
	if n==0 or l<2:
		pen.forward(l)
		return
		
	k(n-1, l/3)
	pen.left(60)
	k(n-1, l/3)
	pen.right(120)
	k(n-1, l/3)
	pen.left(60)
	k(n-1, l/3)
	

def flake(n, l):
	k(n, l); pen.right(120)
	k(n, l); pen.right(120)
	k(n, l); pen.right(120)
