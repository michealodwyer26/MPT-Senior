'''
program to draw random art using circles
'''

from turtle import *
import random
import math

# Make a screen and a pen
pen = Pen()
screen = Screen()

pen.speed(0)
screen.bgcolor("red")

def square(l):
	# draw square
	for i in range(4):
		pen.forward(l);pen.right(90)
		
def spiral(n):
	for i in range(n):
		square(200)
		pen.left(360//n)
		
def snail(n):
	for i in range(n):
		square(200+i+5)
		pen.left(360//n)

def randomCircle():
	# Generate the random radius, position and color
	radius = random.randint(10, 100)
	
	x = random.randint(-400, 400)
	y = random.randint(-300, 300)
	
	red = random.random()
	green = random.random()
	blue = random.random()
	
	screen.bgcolor((red, green, blue))
	
	# set the turtle features and draw
	pen.penup(); pen.goto(x, y); pen.pendown()
	pen.color(red, green, blue)
	pen.begin_fill()

	pen.circle(radius)
	
	pen.end_fill()

snail(50)
	