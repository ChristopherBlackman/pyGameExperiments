from point import Point

class lines():
	def __init__(self,seedListSize,max_y_value,numberOfItterations,roughnessConstant):
		#declare local varibles
		self.head
		self.seedListSize = seedListSize
		self.max_y_value = max_y_value
		self.numberOfItterations = numberOfItterations
		self.roughnessConstant = self.roughnessConstant
		
		#define mountain range
		head = randomLinkedList()
		createMountains()
	
	'''
		create a randomLinkedList of Point as seeds
	'''
	def __randomLinkedList__():
		self.head = Point()
		self.head.set_y_val(random.random()*self.max_y_value)
		temp = self.head
		while numberOfNodes > 0:
			temp.setNext(Point())
			temp = temp.getNext()
			temp.set_y_val(random.random()*rangeOf_y)
			numberOfNodes -= 1
		return
	'''
		create a procedual mountains
	'''
	def __createMountains__(self,node, numberOfRuns,roughConstant):
		i = 1
		while i <= numberOfRuns:
			self.addNodes(node,i,roughConstant)
			i += 1
		return
	'''
		for every other node this will add nodes inbetween
		the average will be part of the calculation for the node + a random amount multipled by a roughConstant
	'''
	def __addNodes__(node,run,roughConstant):
		while node.getNext() is not None:
			newNode = Point()
			averageRandom = (node.get_y_val() + node.getNext().get_y_val())/2 + 200 *random.random() * roughConstant * math.pow(2,-run*roughConstant)
			newNode.set_y_val(averageRandom)
			newNode.setNext(node.getNext())
			node.setNext(newNode)
			node = newNode.getNext()
		return
	'''
		print the linked list into an array formmated string
	'''
	def printNodes(node):
		a = "["
		while node is not None:
			a = a + str(node.get_y_val()) + " "
			node = node.getNext()
		a = a + "]"
		return a
