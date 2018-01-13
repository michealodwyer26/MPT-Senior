'''
program for euro to dollar conversion using the rate = 1.23
'''

from tkinter import *

# Set up the window
root = Tk()
root.title("Money Converter")
root.geometry("300x200+100+100")

# make the interface
convLabel = Label(root, text="Euro to Dollar Converter")
convLabel.grid(row=0, column=1, columnspan=2)

# euro widgets
euroLabel = Label(root, text="Euro")
euroLabel.grid(row=1, column=0)

euroStr = StringVar()
euroEntry = Entry(root, textvariable= euroStr)
euroEntry.grid(row=1, column=1, columnspan=2)

# dollar widgets
dollarLabel = Label(root, text="Dollar")
dollarLabel.grid(row=2, column=0)

dollarStr = StringVar()
dollarEntry = Entry(root, textvariable= dollarStr)
dollarEntry.grid(row=2, column=1, columnspan=2)

# button widgets

def clearF():
	# clear the entrys
	euroStr.set("")
	dollarStr.set("")
	
	return

clearButton = Button(root, text="Clear", command=clearF)
clearButton.grid(row=3, column=1)

def convertF():
	# get the value from eurostr and make it float
	euroAmount = float(euroStr.get())
	# clear euro to dollar using the given rate
	dollarAmount = euroAmount * 1.23
	
	# set the new value to dollarStr
	dollarStr.set(str(dollarAmount))
	
	return

convertButton = Button(root, text="Convert", command=convertF)
convertButton.grid(row=3, column=2)

root.mainloop()












