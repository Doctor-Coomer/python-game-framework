#!/bin/python

import framework

from time import sleep

#import framework
game = framework.game_framework()

#constants
WIDTH  = 500
HEIGHT = 500

#create box
b = game.create_rectangle(x=WIDTH//2 - 25, y=HEIGHT//2 - 25, width=50, height=50)

#create window
game.spawn_window(width=WIDTH, height=HEIGHT, resizable=True)

grabbing:bool = False
while True:
    mouse = game.get_mouse()

    #detect if grabbing
    #and move box
    if not mouse.left:
        grabbing = False
    elif grabbing == True:
        b.x = mouse.x - b.width//2
        b.y = mouse.y - b.height//2
        
    if (mouse.x >= b.x and mouse.x <= b.x+b.width and
        mouse.y >= b.y and mouse.y <= b.y+b.height):
        if mouse.left:
            grabbing = True
    
    sleep(1/60)
