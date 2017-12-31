'''
python program to calculate BMI given the weight and height in a GUI
interface using Tkinter.
'''

# import modules
from tkinter import *
import math

# set up the window/root
root = Tk()
root.geometry("200x100+200+200")
root.title("Metric BMI Calculator")

def clearCallback():
	weightVar.set("")
	heightVar.set("")
	BMIVar.set("")

def convertCallback():
	height = float(heightVar.get())
	weight = float(weightVar.get())
	
	BMI = weight/(height*height)

	BMIVar.set(str(BMI))
	
# set up components/widgets
titleLabel = Label(root, text="Metric BMI Converter")
titleLabel.grid(row=0, column=1, rowspan=1, columnspan=4)

weightLabel = Label(root, text="Weight(kg)")
weightLabel.grid(row=1, column=0, rowspan=1, columnspan=1)

heightLabel = Label(root, text="Height(m)")
heightLabel.grid(row=2, column=0, rowspan=1, columnspan=1)

BMILabel = Label(root, text="BMI")
BMILabel.grid(row=3, column=0, rowspan=1, columnspan=1)

weightVar = StringVar()
weightEntry = Entry(root, textvariable=weightVar)
weightEntry.grid(row=1, column=1, rowspan=1, columnspan=1)

heightVar = StringVar()
heightEntry = Entry(root, textvariable=heightVar)
heightEntry.grid(row=2, column=1, rowspan=1, columnspan=1)

BMIVar = StringVar();
BMICalculationLabel = Label(root, textvariable=BMIVar)
BMICalculationLabel.grid(row=3, column=1, rowspan=1, columnspan=1)
BMIVar.set("")

clearButton = Button(root, text="Clear", command=clearCallback)
clearButton.grid(row=4, column=0, rowspan=1, columnspan=1)

convertButton = Button(root, text="Convert", command=convertCallback)
convertButton.grid(row=4, column=1, rowspan=1, columnspan=1)





# run the main loop for events
root.mainloop()