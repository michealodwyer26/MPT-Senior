# simple interface test

from tkinter import *

root = Tk()
root.title("Interface test")
root.geometry("300x200+100+100")

labelStr = StringVar()
label = Label(root, text="Sorry me, but Sabin does not like monkey business.", textvariable = labelStr)
label.pack()

entryVar = StringVar()
entry = Entry(root, textvariable = entryVar)
entry.pack()

def buttonF():
	# define the action to say hello mpt from the entry name
	
	# get the name from the entry text vars
	name = entryVar.get()
	
	# make the new string to display
	helloStr = "Hello MPT Class from " + name
	
	# place this string to the labelVar
	labelStr.set(helloStr)

button = Button(root, text="say hello", command = buttonF)
button.pack()

root.mainloop()