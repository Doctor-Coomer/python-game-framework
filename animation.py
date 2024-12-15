#!/bin/python

import framework

import time
from math import *
from random import *

game = framework.game_framework();

#constants
WIDTH = 750
HEIGHT = 700

bg = game.create_rectangle(x=0, y=0, width=WIDTH, height=HEIGHT, color=[0,0,255])

game.spawn_window(width=WIDTH, height=HEIGHT, resizable=True);

l1 = game.create_line(x1=0, y1=0, x2=WIDTH, y2=HEIGHT);
l2 = game.create_line(x1=0, y1=HEIGHT, x2=WIDTH, y2=0);

l3 = game.create_line(x1=0, y1=0, x2=0, y2=0)
l4 = game.create_line(x1=0, y1=0, x2=0, y2=0)

l5 = game.create_line(x1=0, y1=0, x2=0, y2=0)
l6 = game.create_line(x1=0, y1=0, x2=0, y2=0)

bt_l1 = game.create_rectangle(x=l1.x1, y=l1.x1, width=30, height=30, color=[255,0,0]);
bb_l1 = game.create_rectangle(x=l1.x2, y=l1.y2, width=30, height=30, color=[255,0,0]);

bt_l2 = game.create_rectangle(x=l2.x1, y=l2.x1, width=30, height=30, color=[0,255,0]);
bb_l2 = game.create_rectangle(x=l2.x2, y=l2.y2, width=30, height=30, color=[0,255,0]);

def distance(p1, p2):
    return sqrt((p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y))

i:int = 0
direction_i:bool = False

h:int = 0
direction_h:bool = False

x:float = 0
while True:
    l1.x1 = i
    l1.x2 = WIDTH - (i%WIDTH)
    l1.y1 = int(abs(cos(x)*200))
    l1.y2 = HEIGHT-int(abs(sin(x)*200))

    bb_l1.x=l1.x2-(bb_l1.width//2)
    bb_l1.y=l1.y2-(bb_l1.height//2)

    bt_l1.x=l1.x1-(bt_l1.width//2)
    bt_l1.y=l1.y1-(bt_l1.height//2)

    
    l2.x1 = int(abs(sin(x)*200))
    l2.x2 = WIDTH-int(abs(cos(x)*200))
    l2.y1 = h
    l2.y2 = HEIGHT - (h%HEIGHT)
    
    bb_l2.x=l2.x2-(bb_l2.width//2)
    bb_l2.y=l2.y2-(bb_l2.height//2)

    bt_l2.x=l2.x1-(bt_l2.width//2)
    bt_l2.y=l2.y1-(bt_l2.height//2)

    l3.x1 = bt_l1.x + (bt_l1.width//2) 
    l3.y1 = bt_l1.y + (bt_l1.height//2)
    l3.x2 = bt_l2.x + (bt_l2.width//2)
    l3.y2 = bt_l2.y + (bt_l2.height//2)

    l4.x1 = bb_l1.x + (bb_l1.width//2) 
    l4.y1 = bb_l1.y + (bb_l1.height//2)
    l4.x2 = bb_l2.x + (bb_l2.width//2)
    l4.y2 = bb_l2.y + (bb_l2.height//2)

    l5.x1 = bb_l1.x + (bb_l1.width//2) 
    l5.y1 = bb_l1.y + (bb_l1.height//2)
    l5.x2 = bt_l2.x + (bt_l2.width//2)
    l5.y2 = bt_l2.y + (bt_l2.height//2)

    l6.x1 = bt_l1.x + (bt_l1.width//2) 
    l6.y1 = bt_l1.y + (bt_l1.height//2)
    l6.x2 = bb_l2.x + (bb_l2.width//2)
    l6.y2 = bb_l2.y + (bb_l2.height//2)
    
    
    if i+1 >= WIDTH: 
        direction_i = True
    elif i <= 0:
        direction_i = False

    if direction_i == True:
        i-=1
    elif direction_i == False:
        i+=1

    if h+1 >= HEIGHT:
        direction_h = True
    elif h <= 0:
        direction_h = False

    if direction_h == True:
        h-=1
    elif direction_h == False:
        h+=1

    new_width_l1:int = int((750*6)/(distance(bb_l1, bt_l1) if distance(bb_l1, bt_l1) > 0 else 0.00000001))
    l1.width=new_width_l1 if new_width_l1 < bt_l1.width-3 else bt_l1.width-3

    new_width_l2:int = int((750*6)/(distance(bb_l2, bt_l2) if distance(bb_l2, bt_l2) > 0 else 0.00000001))
    l2.width=new_width_l2 if new_width_l2 < bt_l2.width-3 else bt_l2.width-3

    new_width_l3:int = int((750*6)/(distance(bt_l1, bt_l2) if distance(bt_l1, bt_l2) > 0 else 0.00000001))
    l3.width=new_width_l3 if new_width_l3 < bt_l1.width-3 else bt_l1.width-3

    new_width_l4:int = int((750*6)/(distance(bb_l1, bb_l2) if distance(bb_l1, bb_l2) > 0 else 0.00000001))
    l4.width=new_width_l4 if new_width_l4 < bb_l1.width-3 else bb_l1.width-3

    new_width_l5:int = int((750*6)/(distance(bb_l1, bt_l2) if distance(bb_l1, bt_l2) > 0 else 0.00000001))
    l5.width=new_width_l5 if new_width_l5 < bb_l1.width-3 else bb_l1.width-3

    new_width_l6:int = int((750*6)/(distance(bt_l1, bb_l2) if distance(bt_l1, bb_l2) > 0 else 0.00000001))
    l6.width=new_width_l6 if new_width_l6 < bt_l1.width-3 else bt_l1.width-3
    
    x+=0.01
    time.sleep(0.005);

    (WIDTH, HEIGHT) = game.get_window_resolution()
    bg.width = WIDTH
    bg.height = HEIGHT
