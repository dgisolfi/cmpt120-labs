#Into to programing
#Author: Daniel Gisolfi
#Date: 11/11/16
#locale.py

class locale:
	#constructor
	def __init__(self, name, description, item):
		self.name = name	#atrributes of player
		self.description = description
		self.isVisited = False
		self.item = item

	def render(self):
		if isVisited == True:
			self.description == "You have returned to "
			print(self.description, self.name)

	def removeItem(self, item):
		if self.item == item:
			self.item = None
	def visit(self):
		self.isVisited = True


