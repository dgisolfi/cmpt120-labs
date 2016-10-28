colors = ["blue","black","red","yellow","white","gray"]

def showTitle():
	pass

def promptForColor():
	return colors[2]

def confirmColor():
	return True

def containsElement():
	return True

def praiseUser():
	pass

def ridiculeUser():
	pass

def main():
	showTitle()

	while True:
		cmd = input("enter the name of a color: ").lower()
		confirm = input("Are you sure this is the color you would like to enter: ").lower()

		if confirm == "yes":
			if cmd in colors:
				print("good, that is a great color")
			else:
				print("bad, why would you choose that color")
		else:
			continue

main()
