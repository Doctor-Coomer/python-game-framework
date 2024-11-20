#!/bin/python
#this file is an example

import framework #import the framework

import time
from math import *

game = framework.game_framework(); #create a game instance

#constants
WIDTH = 300;
HEIGHT = 300;

LEFT = False;
RIGHT = True;

PAD_SPEED = 6;
BALL_SPEED = 7;

#sprites are rendered in order of when they are defined

#player 1
p1 = game.create_rectangle(x=10, y=HEIGHT//2 - (40), width=10, height=90, color=[0,0,255])
p1m = game.create_line(x1=p1.x, y1=(p1.y+p1.y+p1.height)//2, x2=p1.x+p1.width, y2=(p1.y+p1.y+p1.height)//2, width=2, color=[190,190,190])

#player 2
p2 = game.create_rectangle(x=WIDTH-30, y=HEIGHT//2 - (40), width=10, height=90, color=[255,0,0])
p2m = game.create_line(x1=p2.x, y1=(p2.y+p2.y+p2.height)//2, x2=p2.x+p2.width, y2=(p2.y+p2.y+p2.height)//2, width=2, color=[190,190,190])

#ball
ball_dir = game.create_line(x1=0, y1=HEIGHT//2, x2=WIDTH, y2=HEIGHT//2, color=[25,200,0])
ball = game.create_rectangle(x=WIDTH//2, y=HEIGHT//2, width=5, height=5)

#creates a new window
game.spawn_window(width=WIDTH, height=HEIGHT);

#menu text
start_text = game.create_text(x=WIDTH//2 - (50), y=HEIGHT//2-50, text="Press Space")

#pause game until they are ready
while game.is_key_down(" ") != True:
    time.sleep(0.025);
start_text.delete();

#game logic loop
horizontal_direction:bool = LEFT;
virtical_slope:float = 0.0;
y_intercept = ball.y;
while True:
    #get key inputs
    arrowkeys = game.get_arrow_keys();
    
    wkey:bool = game.is_key_down("w");
    skey:bool = game.is_key_down("s");

    #game end detection, and reset
    if ball.x <= 0:
        p1_text = game.create_text(x=WIDTH//2 - (50), y=HEIGHT//2, text="Player 2 wins", color=[255,0,0]);
        restart_text = game.create_text(x=WIDTH//2 - (50), y=HEIGHT//2 - (35), text="Press Space to Restart")
        while game.is_key_down(" ") != True:
            time.sleep(0.025);
        restart_text.delete();
        p1_text.delete();
        ball.x=WIDTH//2;
        ball.y=HEIGHT//2;
        horizontal_direction:bool = LEFT;
        virtical_slope:float = 0.0;
        y_intercept = ball.y;
        p1.x=10;
        p1.y=HEIGHT//2 - (40);
        p1m.x1=p1.x
        p1m.y1=(p1.y+p1.y+p1.height)//2
        p1m.x2=p1.x+p1.width
        p1m.y2=(p1.y+p1.y+p1.height)//2
        p2.x=WIDTH-30
        p2.y=HEIGHT//2 - (40);
        p2m.x1=p2.x
        p2m.y1=(p2.y+p2.y+p2.height)//2
        p2m.x2=p2.x+p2.width
        p2m.y2=(p2.y+p2.y+p2.height)//2
    elif ball.x >= WIDTH:
        p1_text = game.create_text(x=WIDTH//2 - (50), y=HEIGHT//2, text="Player 1 wins", color=[0,0,255])
        restart_text = game.create_text(x=WIDTH//2 - (50), y=HEIGHT//2 - (35), text="Press Space to Restart")
        while game.is_key_down(" ") != True:
            time.sleep(0.025);
        restart_text.delete();
        p1_text.delete();
        ball.x=WIDTH//2;
        ball.y=HEIGHT//2;
        horizontal_direction:bool = LEFT;
        virtical_slope:float = 0.0;
        y_intercept = ball.y;
        p1.x=10;
        p1.y=HEIGHT//2 - (40);
        p1m.x1=p1.x
        p1m.y1=(p1.y+p1.y+p1.height)//2
        p1m.x2=p1.x+p1.width
        p1m.y2=(p1.y+p1.y+p1.height)//2
        p2.x=WIDTH-30
        p2.y=HEIGHT//2 - (40);
        p2m.x1=p2.x
        p2m.y1=(p2.y+p2.y+p2.height)//2
        p2m.x2=p2.x+p2.width
        p2m.y2=(p2.y+p2.y+p2.height)//2

    #player input for paddles
    if arrowkeys.up == True and arrowkeys.down == True:
        ... #do nothing
    elif arrowkeys.up == True and p2.y >= 0:
        p2.y-=PAD_SPEED;
        p2m.y1-=PAD_SPEED;
        p2m.y2-=PAD_SPEED;
    elif arrowkeys.down == True and p2.y+p2.height <= HEIGHT:
        p2.y+=PAD_SPEED;
        p2m.y1+=PAD_SPEED;
        p2m.y2+=PAD_SPEED;
        
    if wkey == True and skey == True:
        ... #do nothing
    elif wkey == True and p1.y >= 0:
        p1.y-=PAD_SPEED;
        p1m.y1-=PAD_SPEED;
        p1m.y2-=PAD_SPEED;
    elif skey == True and p1.y+p1.height <= HEIGHT:
        p1.y+=PAD_SPEED;
        p1m.y1+=PAD_SPEED;
        p1m.y2+=PAD_SPEED;
        
    #ball detection with paddles
    if ((ball.x <= p1.x+p1.width or ball.x+ball.width <= p1.x+p1.width) and (ball.x >= p1.x or ball.x+ball.width >= p1.x)) and ball.y >= p1.y and ball.y <= p1.y+p1.height:
        horizontal_direction = RIGHT;
        new_virtical_slope:float = ((ball.y-p1m.y1)/(p1m.y1-p1.y))/2;
        y_intercept = (virtical_slope*ball.x)+y_intercept-(new_virtical_slope*ball.x);
        virtical_slope = new_virtical_slope;
    if ((ball.x >= p2.x-(p2.width//2)+5 or ball.x+ball.width >= p2.x-(p2.width//2)+5) and (ball.x <= p2.x or ball.x+ball.width <= p2.x)) and ball.y >= p2.y and ball.y <= p2.y+p2.height:
        horizontal_direction = LEFT;
        new_virtical_slope:float = ((p2m.y1-ball.y)/(p1m.y1-p1.y))/2;
        y_intercept = (virtical_slope*ball.x)+y_intercept-(new_virtical_slope*ball.x);
        virtical_slope = new_virtical_slope;
        
    #ball detection with ceiling and floor
    if ball.y >= HEIGHT or ball.y <= 0:
        new_virtical_slope:float = virtical_slope * -1;
        y_intercept = (virtical_slope*ball.x)+y_intercept-(new_virtical_slope*ball.x);
        virtical_slope = new_virtical_slope;
        
    #move the ball
    if horizontal_direction == LEFT:
        ball.x-=BALL_SPEED;
    elif horizontal_direction == RIGHT:
        ball.x+=BALL_SPEED;

    #y = mx+b
    ball.y=int(virtical_slope*ball.x+y_intercept);

    #update ball direction helper
    ball_dir.y1=int(y_intercept);
    ball_dir.y2=int(virtical_slope*ball_dir.x2+y_intercept);

    time.sleep(0.025); #1/40 of a second
