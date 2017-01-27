import pygame
import random
import math
from pygame.locals import *
from point import Point

def main():
	pygame.init()
	
	#colors
	RED   = (250,0,0)
	GREEN = (0,250,0)
	PURPLE  = (50,0,100)
	BLACK = (0,0,0)
	
	#setup display
	screen = pygame.display.set_mode((1200, 400))
	pygame.display.set_caption('Mid-Point Displacemnt Algorithm 2D')
	pygame.mouse.set_visible(1)
	
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill(BLACK)
	
	#set up mountian range
	head = randomLinkedList(3,100)
	createMountains(head,5,0.75)
	
	diff_x = 15
	drawLinesToScreen(head,background,RED,PURPLE,diff_x,0,300,3)
	
	#add the mountain to background
	screen.blit(background,(0,0))
	
	while 1:
		#Handle Input Events
		for event in pygame.event.get():
			if event.type == QUIT:
				return
		pygame.display.update()

'''
	create a randomLinkedList of Point as seeds
'''
def randomLinkedList(numberOfNodes,rangeOf_y):
	head = Point()
	head.set_y_val(random.random()*rangeOf_y)
	temp = head
	while numberOfNodes > 0:
		temp.setNext(Point())
		temp = temp.getNext()
		temp.set_y_val(random.random()*rangeOf_y)
		numberOfNodes -= 1
	return head

'''
	draws the nodes in the list to the screen
	nodes with positive slope will be an uphill color, nodes with negative will be a down hill color
'''
def drawLinesToScreen(node, background,uphillColor,DownhillColor,diff_x,screenPos_x,drawHeight,width):
	while node.getNext() is not None :
		if node.get_y_val() - node.getNext().get_y_val() < 0:
			pygame.draw.line(background,uphillColor,(screenPos_x,drawHeight - node.get_y_val()),(screenPos_x + diff_x,drawHeight - node.getNext().get_y_val()),width)
		else:
			pygame.draw.line(background,DownhillColor,(screenPos_x,drawHeight - node.get_y_val()),(screenPos_x + diff_x,drawHeight - node.getNext().get_y_val()),width)
		screenPos_x += diff_x
		node = node.getNext()
'''
	for every other node this will add nodes inbetween
	the average will be part of the calculation for the node + a random amount multipled by a roughConstant
'''
def addNodes(node,run,roughConstant):
	while node.getNext() is not None:
		newNode = Point()
		averageRandom = (node.get_y_val() + node.getNext().get_y_val())/2 + 200 *random.random() * roughConstant * math.pow(2,-run*roughConstant)
		newNode.set_y_val(averageRandom)
		newNode.setNext(node.getNext())
		node.setNext(newNode)
		node = newNode.getNext()
	return
'''
	create a procedual mountains
'''
def createMountains(node, numberOfRuns,roughConstant):
	i = 1
	while i <= numberOfRuns:
		addNodes(node,i,roughConstant)
		i += 1
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

main()