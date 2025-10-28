import framework
import sprites

import time
from math import *
from random import *

#constants
WIDTH  = 500;
HEIGHT = 500;

t = time.time()

game = framework.game_framework(); #create a game instance

game.spawn_window(width=WIDTH, height=HEIGHT, draw_stepping=True);

functions:str = ["sin(x)", "cos(x)"]

scale = 60;
STEP = 1;

scalex = int(scale);
scaley = int(scale);

def step_and_wait():
    game.step_window();
    while game.is_drawing():
        time.sleep(0.0000000001)


game.create_rectangle(0,0,WIDTH,HEIGHT,color=[255,255,255]);

time.sleep(0.1);

my_font = game.create_font("9x15bold");

loading_text1 = game.create_text(x=3, y=16, text="Loading", font=my_font);
loading_text2 = game.create_text(x=3, y=15, text="Loading", font=my_font);
loading_text3 = game.create_text(x=2, y=16, text="Loading", font=my_font);
loading_text = game.create_text(x=2, y=15, text="Loading", color=[0,255,0], font=my_font);

step_and_wait();

game.create_line(x1=WIDTH//2+1, y1=HEIGHT, x2=WIDTH//2+1, y2=0, width=1, color=[255//2, 255//2, 255//2]);
game.create_line(x1=0, y1=HEIGHT//2+1, x2=WIDTH, y2=HEIGHT//2+1, width=1, color=[255//2, 255//2, 255//2]);

game.create_line(x1=WIDTH//2, y1=HEIGHT, x2=WIDTH//2, y2=0, width=1);
game.create_line(x1=0, y1=HEIGHT//2, x2=WIDTH, y2=HEIGHT//2, width=1);

if scale > 1:
    # Draw marks

    # Q1
    for y in range(1,HEIGHT//scaley):
        for x in range(1,WIDTH//scalex):
            game.create_line(WIDTH//2+1, HEIGHT//2 - y * scaley, WIDTH, HEIGHT//2 - y * scaley, width=1, color=[255//2, 255//2, 255//2]);
            game.create_line(WIDTH//2 + x * scalex, HEIGHT//2, WIDTH//2 + x * scalex, 0, width=1, color=[255//2, 255//2, 255//2]);

    # Q3
    for y in range(1,HEIGHT//scaley):
        for x in range(1,WIDTH//scalex):
            game.create_line(0, HEIGHT//2 + y * scaley, WIDTH//2, HEIGHT//2 + y * scaley, width=1, color=[255//2, 255//2, 255//2]);
            game.create_line(WIDTH//2 - x * scalex, HEIGHT//2+1, WIDTH//2 - x * scalex, HEIGHT, width=1, color=[255//2, 255//2, 255//2]);

    # Q2 
    for y in range(1,HEIGHT//scaley):
        for x in range(1,WIDTH//scalex):
            game.create_line(0, HEIGHT//2 - y * scaley, WIDTH//2, HEIGHT//2 - y * scaley, width=1, color=[255//2, 255//2, 255//2]);
            game.create_line(WIDTH//2 - x * scalex, HEIGHT//2, WIDTH//2 - x * scalex, 0, width=1, color=[255//2, 255//2, 255//2]);

    # Q4
    for y in range(1,HEIGHT//scaley):
        for x in range(1,WIDTH//scalex):
            game.create_line(WIDTH//2+1, HEIGHT//2 + y * scaley, WIDTH, HEIGHT//2 + y * scaley, width=1, color=[255//2, 255//2, 255//2]);
            game.create_line(WIDTH//2 + x * scalex, HEIGHT//2, WIDTH//2 + x * scalex, HEIGHT, width=1, color=[255//2, 255//2, 255//2]);

    for x in range(1,WIDTH//scalex):
        if scalex > 16:
            game.create_text(WIDTH//2 + x * scalex + 2, HEIGHT//2 - 1 + 14, str(x));

    for x in range(1,WIDTH//scalex):
        if scalex > 16:
            game.create_text(WIDTH//2 + -x * scalex + 2, HEIGHT//2 - 1 + 14, str(-x));

    for y in range(1,HEIGHT//scaley):
        if scaley > 16:
            game.create_text(WIDTH//2 + 3, HEIGHT//2 - y * scaley + 12, str(y));

    for y in range(1,HEIGHT//scaley):
        if scaley > 16:
            game.create_text(WIDTH//2 + 3, HEIGHT//2 + y * scaley + 12, str(-y));

    """
    # Q2
    for y in range(HEIGHT//scaley):
        for x in range(WIDTH//scalex):
            game.create_point(WIDTH//2 + -x * scalex, -y * scaley + HEIGHT//2);

    # Q1
    for y in range(HEIGHT//scaley):
        for x in range(WIDTH//scalex):
            game.create_point(WIDTH//2 + x * scalex, -y * scaley + HEIGHT//2);
            
    # Q4
    for y in range(HEIGHT//scaley):
        for x in range(WIDTH//scalex):
            game.create_point(WIDTH//2 + x * scalex, y * scaley + HEIGHT//2);

    # Q3
    for y in range(HEIGHT//scaley):
        for x in range(WIDTH//scalex):
            game.create_point(WIDTH//2 + -x * scalex, y * scaley + HEIGHT//2);
    """
    
    # Axis dots
    """
    for y in range(1,HEIGHT//scaley):
        game.create_point(WIDTH//2 + 1, -y * scaley + HEIGHT//2);

    for y in range(1,HEIGHT//scaley):
        game.create_point(WIDTH//2 + 1, y * scaley + HEIGHT//2);

    for x in range(1,HEIGHT//scalex):
        game.create_point(WIDTH//2 + x * scalex, HEIGHT//2 - 1);
        #if scalex > 8:
        #    game.create_text(WIDTH//2 + x * scalex, HEIGHT//2 - 1 + 14, str(x));

    for x in range(1,HEIGHT//scalex):
        game.create_point(WIDTH//2 + -x * scalex, HEIGHT//2 - 1);
        #if scalex > 8:
        #    game.create_text(WIDTH//2 + -x * scalex, HEIGHT//2 - 1 + 14, str(-x));
    """

loading_text.delete();
loading_text1.delete();
loading_text2.delete();
loading_text3.delete();

graphing_text1 = game.create_text(x=3, y=16, text="Graphing....", font=my_font);
graphing_text2 = game.create_text(x=3, y=15, text="Graphing....", font=my_font);
graphing_text3 = game.create_text(x=2, y=15, text="Graphing....", font=my_font);
graphing_text = game.create_text(x=2, y=15, text="Graphing....", color=[255,0,255], font=my_font);

step_and_wait();
    
def round(n):
    if isinstance(n, complex):
        return n;
    
    if n < 0:
        return int(n-0.5)
    else:
        return int(n+0.5)
    
# Draw the function        
def norm_to_pixel(function:str):
    y:float = HEIGHT+1;
    try:
        y = eval(function);
    except ValueError:
        print(f"Imaginary point at x = {x}");
        y = HEIGHT+1;

    return  HEIGHT - round(y * scaley);
    


lines:list = [];

for function in functions:
    points:list = [];
    x:float = WIDTH//2 * -1;
    while x < WIDTH//2:
        y:int = norm_to_pixel(function) - HEIGHT//2;
        if (not isinstance(y, complex) and y > -HEIGHT and y < HEIGHT*2):
            points.append((round(WIDTH//2 + x * scalex), y));
        x+=STEP/(scale//2);
    lines.append(points);

colors:list = [[0,0,255], [255,0,0], [0,255,0], [0,255,255], [255,0,255]];
c:int = 0;

for line in lines:
    i:int = 1;
    while i < len(line):
        x1:int = int(line[i-1][0]);
        y1:int = int(line[i-1][1]);
        
        x2:int = int(line[i][0]);
        y2:int = int(line[i][1]);
    
        game.create_line(x1, y1, x2, y2, color=colors[c%len(colors)], width=2);
        #game.create_point(x1, y1, color=[255,0,0]);
        i+=1;
    c+=1;

    #time.sleep(0.005)

graphing_text1.delete();
graphing_text2.delete();
graphing_text3.delete();
graphing_text.delete();


time_delta:float = (time.time() - t);

calculated_text1 = game.create_text(x=3, y=16, text=f"Calculated in {'%.2f' % time_delta} seconds", font=my_font);
calculated_text2 = game.create_text(x=3, y=15, text=f"Calculated in {'%.2f' % time_delta} seconds", font=my_font);
calculated_text3 = game.create_text(x=2, y=16, text=f"Calculated in {'%.2f' % time_delta} seconds", font=my_font);
calculated_text = game.create_text(x=2, y=15, text=f"Calculated in {'%.2f' % time_delta} seconds", color=[0,0,255], font=my_font);

print(f"The calculations took {'%.2f' % (time.time() - t)} seconds");

step_and_wait();

time_delta = (time.time() - t);

finish_text1 = game.create_text(x=3, y=16 + my_font.height + 3, text=f"Rendered in {'%.2f' % time_delta} seconds", font=my_font);
finish_text2 = game.create_text(x=3, y=15 + my_font.height + 3, text=f"Rendered in {'%.2f' % time_delta} seconds", font=my_font);
finish_text3 = game.create_text(x=2, y=16 + my_font.height + 3, text=f"Rendered in {'%.2f' % time_delta} seconds", font=my_font);
finish_text = game.create_text(x=2, y=15 + my_font.height + 3, text=f"Rendered in {'%.2f' % time_delta} seconds", color=[0,255,255], font=my_font);

print(f"The rendering took {'%.2f' % (time.time() - t)} seconds");

step_and_wait();
