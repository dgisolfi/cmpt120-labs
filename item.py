#Into to programing
#Author: Daniel Gisolfi
#Date: 11/11/16
#item.py

class item:

	def __init__(self, name, description):
		self.name = name	#atrributes of player
		self.description = description
	
	def render(self):
		print(self.render)

def containsItem(self, arg):
	items = ["keycard","flashlight","phone"]
	
	if arg in items:
		return True
