colors = ["blue","black","red","yellow","white","gray"]

def showTitle():
	print("Color Preference Evaluator")

def promptForColor():
	global cmd
	cmd = input("enter the name of a color: ")
	confirm = input("Are you sure this is the color you would like to enter: ")
	if confirm == "yes":
		cmd.upper()
		cmd.strip()
		return cmd
	else:
		continue
	
def confirmColor():
	confirm = input("you entered the color " + cmd + " Is this correct (Y/N)?").upper()
	if confirm == "Y":
		return True
	else:
		return False

def containsElement():
	if cmd in colors:
		return True
	else:
		return False

def praiseUser():
	print("good")

def ridiculeUser():
	print("bad")

def main():
	showTitle()
	
	while True:
		color = promptForColor()
        if (confirmColor(color)):
            break
        if (containsElement(colors, color)):
        	praiseUser()
        else:
            ridiculeUser()

main()
