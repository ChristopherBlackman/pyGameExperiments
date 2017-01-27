import random
import math
import pygame
import time
from Point import Point
from array import *
from pygame.locals import *


#colors
RED   = (250,0,0)
GREEN = (0,250,0)
PURPLE  = (100,50,100)
BLACK = (0,0,0)
COLOR = (100,0,0)

# screen options
WIDTH  = 90
HEIGHT = 20
SCALE  = 20
SEED   = 622821

#globals
point_map = Point()
background = None
screen     = None 


def main():

    pygame.init()

    #setup display
    global screen
    screen = pygame.display.set_mode((WIDTH*SCALE, HEIGHT*SCALE))
    pygame.display.set_caption('Maze_gen_v_1')
    pygame.mouse.set_visible(1)

    global background 
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)


    global point_map
    random.seed(SEED)

    while True:
        point_map = Point()
        graph = init_rand_arrya()
        p = (int(WIDTH/2),int(HEIGHT/2))
        DFS(graph,p,p) 
        background.fill(BLACK)
        

    update_screen()

    while True:
        #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            update_screen()

def update_screen():
    screen.blit(background,(4,4))
    pygame.display.update()


# v = (x,y)
def DFS(G,v,last,depth=0):
    if(not EXSISTS_IN_GRAPH(G,v)):
        return 
    color_1  = 0#int(100*(abs(math.sin(math.radians(depth/2)))));
    color_2  = int(100*(abs(math.sin(math.radians(depth/4)))));
    color_3  = int(100*(abs(math.sin(math.radians(depth/8)))));
    draw_line_to_scale(last,v,(color_3,color_1,color_2)) 
    time.sleep(0.01)
    
    point_map[v] = True
    points = lable_points(G,create_cardinal_points(v))
    points = sorted(points,key= lambda item:item[1])

    for point in points:
        if(not point_map[point[0]]):
            DFS(G,point[0],v,depth+1)

def compare_points():
    pass

def draw_line_to_scale(v_1,v_2,color=PURPLE):
    point_a = (v_1[0]*SCALE,v_1[1]*SCALE)
    point_b = (v_2[0]*SCALE,v_2[1]*SCALE)
    pygame.draw.line(background,color,point_a,point_b,4)
    update_screen()

def lable_points(G,points):
    arr = []
    x = 0
    y = 1
    for point in points:
        if(EXSISTS_IN_GRAPH(G,point)):
             arr.append((point,G[point[y]][point[x]])) 
    return arr

def create_cardinal_points(v):
    up   = (v[0],v[1]+1)
    down = (v[0],v[1]-1)
    left = (v[0]-1,v[1])
    right= (v[0]+1,v[1])
    return [up,down,left,right]
# v = (x,y)
def EXSISTS_IN_GRAPH(G,v):
    x = 0
    y = 1
    return v[x] < WIDTH and v[x] >= 0 and v[y] < HEIGHT and v[y] >= 0

def init_rand_arrya():
    width = WIDTH
    height = HEIGHT
    my_array = []
    for i in range(0,height):
        elements = [];
        for j in range(0,width):
            elements.append(random.randint(0,999))
        my_array.append(elements)
    return my_array

main()

