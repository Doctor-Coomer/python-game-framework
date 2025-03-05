#!/bin/python

import framework

from time import sleep

game = framework.game_framework()

WIDTH = 600
HEIGHT = 600

b_arr = []

for i in range(WIDTH//100):
    for h in range(HEIGHT//100):
        b_arr.append(game.create_rectangle(x=i*100, y=h*100, width=100, height=100, color=[255, i*40%255, h*50%255]))

game.spawn_window(width=WIDTH, height=HEIGHT)

start_text = game.create_text(x=20, y=20, text="Press space to play and restart", color=[0, 255, 0])

while game.is_key_down(" ") != True:
    sleep(1/60);
start_text.delete();
    
while True:
    mouse = game.get_mouse()

    if game.is_key_down(' '):
        for b in b_arr:
            b.color = [255, 255, 255]
            b.delete()
        
        b_arr = []
        for i in range(WIDTH//100):
            for h in range(HEIGHT//100):
                b_arr.append(game.create_rectangle(x=i*100, y=h*100, width=100, height=100, color=[255, i*40%255, h*50%255]))


    for b in b_arr:
        if (mouse.x >= b.x and mouse.x <= b.x+b.width and
            mouse.y >= b.y and mouse.y <= b.y+b.height):
            if mouse.left:
                b.color = [255, 255, 255]
    
    sleep(1/60)
