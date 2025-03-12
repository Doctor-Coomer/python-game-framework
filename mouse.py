#!/bin/python

import framework

from time import sleep

#import framework
game = framework.game_framework()

#constants
WIDTH = 700
HEIGHT = 700

BOX_WIDTH = 0
for i in range(WIDTH//(WIDTH//100), 1, -1):
    if WIDTH%i == 0:
        BOX_WIDTH = i
        break

BOX_HEIGHT = 0
for i in range(HEIGHT//(HEIGHT//100), 1, -1):
    if HEIGHT%i == 0:
        BOX_HEIGHT = i
        break


    
VIRTICAL_FADE = 40
HORIZONTAL_FADE = 40


#initialize the array
b_arr = [] #2D array
for i in range(WIDTH//BOX_WIDTH):
    b_tmp = []
    for h in range(HEIGHT//BOX_HEIGHT):
        b_tmp.append(game.create_rectangle(x=i*BOX_WIDTH, y=h*BOX_HEIGHT, width=BOX_WIDTH, height=BOX_HEIGHT, color=[255, i*VIRTICAL_FADE%255, h*HORIZONTAL_FADE%255]))
    b_arr.append(b_tmp)
    
#menu text
start_text = game.create_text(x=20, y=20, text="Press space to play and restart", color=[0, 255, 0])
start_text_instruction = game.create_text(x=20, y=35, text="Click on squares to delete them", color=[0, 255, 0])

# FPS display
fps = game.create_text(x=20, y=HEIGHT-15, text="FPS: -", color=[0, 0, 0])

#display window
game.spawn_window(width=WIDTH, height=HEIGHT)

pressed:bool = False

#pause until they press space
while game.is_key_down(" ") != True:
    sleep(1/60);
start_text.delete();
start_text_instruction.delete();
pressed = True

#main gameplay loop
while True:
    if (game.get_window_fps() != -1):
        fps.text = "FPS: " + str(game.get_window_fps())

    mouse = game.get_mouse()

    #if they press space then restart
    if game.is_key_down(' ') == True and pressed == False:
        pressed = True
        for i in range(len(b_arr)):
            for h in range(len(b_arr[i])):
                b_arr[i][h].color = [255, i*VIRTICAL_FADE%255, h*HORIZONTAL_FADE%255]
    elif game.is_key_down(' ') == False and pressed == True:
        pressed = False

    #detect if they are hovering over any squares
    for bb in b_arr:
        for b in bb:
            if (mouse.x >= b.x and mouse.x <= b.x+b.width and
                mouse.y >= b.y and mouse.y <= b.y+b.height):
                if mouse.left:
                    b.color = [255, 255, 255]
    
    sleep(1/60)
