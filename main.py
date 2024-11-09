#!/bin/python
#this file is an example

import framework #import the framework

import time

game = framework.game_framework(); #create a game instance

#constants
WIDTH = 550
HEIGHT = 450

#sprites are rendered in order of definition
#rendered first
l = game.create_line(x1=0, y1=0, x2=WIDTH, y2=HEIGHT, color=(0,0,0));

#creates a new window
game.spawn_window(width=WIDTH, height=HEIGHT);

#will fail to create a second window
game.spawn_window(width=WIDTH, height=HEIGHT); #logs a warning

#game logic loop
i:int = 2;
while True:
     l.x2 = game.window_resolution()[0]
     l.y2 = game.window_resolution()[1]
     l.width = i%50+2;
     i+=1;
     time.sleep(0.025)
