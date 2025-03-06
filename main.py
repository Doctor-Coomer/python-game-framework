#!/bin/python
#this file is an example

import framework #import the framework

import time
from math import *

game = framework.game_framework(); #create a game instance

#constants
WIDTH = 550;
HEIGHT = 450;

#sprites are rendered in order of definition

#rendered first
l = game.create_line(x1=0, y1=0, x2=WIDTH, y2=HEIGHT, color=[100,100,100], width=30, style="dash");

#gets rendered second, and on top of the first line
l2 = game.create_line(x1=WIDTH, y1=0, x2=0, y2=HEIGHT, color=[0,255,255], width=20);

#rendered last, and third, on top of the previous sprites
b = game.create_rectangle(x=WIDTH//2, y=HEIGHT//2, width=100, height=100, color=[255,0,0])

#creates a new window
game.spawn_window(width=WIDTH, height=HEIGHT, color=[0,0,0]);

#will fail to create a second window
game.spawn_window(width=WIDTH, height=HEIGHT); #logs a warning

t = game.create_text(x=40, y=10, text="FPS: -", color=[255,255,255])

#game logic loop
while True:
    if (game.get_window_fps() != -1):
        #t.y = game.get_window_fps()
        t.text = "FPS: " + str(game.get_window_fps())

    if game.is_key_down("w") == True and game.is_key_down("s") == True:
        ...
    elif game.is_key_down("w"):
        b.y-=6;
    elif game.is_key_down("s"):
        b.y+=6;

        
    if game.is_key_down("a") == True and game.is_key_down("d") == True:
        ... 
    elif game.is_key_down("a"):
        b.x-=6;
    elif game.is_key_down("d"):
        b.x+=6;
        
    time.sleep(1/30);
