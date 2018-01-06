from tkinter import *

## construct the Tk window

root = Tk()
root.geometry("300x300+200+200")
root.title("Converter")

## define functions
def onClear():
	# clear the entries
	euroStr.set("")
	currencyStr.set("")
# end onClear

def onConvert():
	euro = float(euroStr.get())
	
	rate = 1
	# choose the rate based on selection
	if currencyLabel.get() == "Dollar":
		rate = 1.2
	elif currencyLabel.get() == "Pound":
		rate = 0.88
	elif currencyLabel.get() == "Yen":
		rate = 136.06
	# end if
	
	# convert euro to chosen currency
	currency = euro * rate
	
	# pass currency to currencyStr
	currencyStr.set(str(currency))
	
# end onConvert

## make the interface
titleLabel = Label(root, text = "Money Converter")
titleLabel.grid(row = 0, column = 0, columnspan = 2)

euroLabel = Label(root, text = "Euro")
euroLabel.grid(row = 1, column = 0)

# drop down menu
currencyLabel = StringVar()
currencyLabel.set("Dollar") # default value

currencySelect = OptionMenu(root, currencyLabel, "Dollar", "Pound", "Yen")
currencySelect.grid(row = 2, column = 0)

euroStr = StringVar()
euroEntry = Entry(root, textvariable = euroStr)
euroEntry.grid(row = 1, column = 1)

currencyStr = StringVar()
currencyEntry = Entry(root, textvariable = currencyStr)
currencyEntry.grid(row = 2, column = 1)

## buttons
clearButton = Button(root, text = "Clear", command = onClear)
clearButton.grid(row = 3, column = 0)

convertButton = Button(root, text = "Convert", command = onConvert)
convertButton.grid(row = 3, column = 1)


root.mainloop()