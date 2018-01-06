from tkinter import *

## construct the Tk window

root = Tk()
root.geometry("300x200+200+200")
root.title("Basic List")

## define function
def listChoice():
	index = coloursList.curselection()[0]
	colour = colours[index]
	
	labelVar.set(colour)
	mainLabel.configure(fg = colour)
# end def
	
# end def

## colour change word
labelVar = StringVar()
mainLabel = Label(root, textvariable = labelVar, font = ("Heletica", 16))
mainLabel.grid(row = 1, column = 3)
labelVar.set("Colour")

## create list
colours = ["Red", "Blue", "Green", "Yellow"]

coloursList = Listbox(root)

for i in colours:
	coloursList.insert(END, i)
	
coloursList.grid(row = 1, column = 0, rowspan = 1, columnspan = 1)

chooseButton = Button(root, text = "Choose", command = listChoice)
chooseButton.grid(column = 0, row = 2)
root.mainloop()