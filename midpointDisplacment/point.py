'''
class : linked list
description : node for storing a point
properties : None
methods :
	setNext(node)
	getNext()
	set_y_val(y)
	get_y_val()
'''
class Point:
	def __init__(self):
		self.y = 0
		self.next = None
		return
	def setNext(self, node):
		if isinstance(node,Point):
			self.next = node
		return
	def getNext(self):
		return self.next
	def get_y_val(self):
		return self.y
	def set_y_val(self,y):
		self.y = y
