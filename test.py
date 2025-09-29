import framework

import time
import math

#constants
WIDTH  = 1000;
HEIGHT = 743;

game = framework.game_framework(); #create a game instance

game.spawn_window(width=WIDTH, height=HEIGHT, draw_stepping=True);

m = HEIGHT/WIDTH;

#m = -0.01;

game.create_line(x1=WIDTH//2, y1=HEIGHT, x2=WIDTH//2, y2=0, width=1);
game.create_line(x1=0, y1=HEIGHT//2, x2=WIDTH, y2=HEIGHT//2, width=1);

FRAME_WIDTH = 50
FRAME_HEIGHT = 10

for x in range(1, FRAME_WIDTH+1):
    a = ((WIDTH//2)//FRAME_WIDTH)
    game.create_point(WIDTH//2+x*a - 1, HEIGHT//2-1);
    game.create_text(WIDTH//2+x*a, HEIGHT//2+11, str(x))

    a = -((WIDTH//2)//FRAME_WIDTH)
    game.create_point(WIDTH//2+x*a, HEIGHT//2-1);
    game.create_text(WIDTH//2+x*a, HEIGHT//2+11, str(-x))

"""
for x in range(0, WIDTH):
    y:int = int(-m*((x-WIDTH//2)**2)+HEIGHT//2);
    a = -((WIDTH//2)//FRAME_WIDTH)
    game.create_point(x,y);
"""

for y in range(0, HEIGHT):
    x:int = int(math.sqrt( ((y-HEIGHT//2)/-m) if ((y-HEIGHT//2)/-m) >= 0 else 0 ) + WIDTH//2);
    game.create_point(x,y-30);
    x = int(-math.sqrt( ((y-HEIGHT//2)/-m) if ((y-HEIGHT//2)/-m) >= 0 else 0 ) + WIDTH//2)
    game.create_point(x,y);

game.step_window();
