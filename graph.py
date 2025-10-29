#!/bin/python
import framework
import sprites

import time
from math import *
from random import *

#constants
WIDTH  = 800;
HEIGHT = 600;

t = time.time()

game = framework.game_framework(); #create a game instance

game.spawn_window(width=WIDTH, height=HEIGHT, draw_stepping=True);

#functions:str = ["cos(sin(5*x))*1.2**x+2", "cos(sin(5*x))*1.2**x", "cos(sin(5*x))*1.2**x-2", "cos(sin(5*x))*1.2**x-4", "cos(sin(5*x))*1.2**x-6"]
#functions:str = ["exp(x)"]
#functions:str = ["(x-2)**3+(5-x)**2-x-6"]
functions:str = ["sin(x)"]

MAGNITUDE = 60;
STEP = 1;

MAGNITUDEx = int(MAGNITUDE);
MAGNITUDEy = int(MAGNITUDE);

def step_and_wait():
    game.step_window();
    while game.is_drawing():
        time.sleep(0.0000000001)


game.create_rectangle(0,0,WIDTH,HEIGHT,color=[255,255,255]);

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

if MAGNITUDE > 1:
    # Draw marks

    # Q1
    for y in range(1,HEIGHT//MAGNITUDEy):
        for x in range(1,WIDTH//MAGNITUDEx):
            game.create_line(WIDTH//2+1, HEIGHT//2 - y * MAGNITUDEy, WIDTH, HEIGHT//2 - y * MAGNITUDEy, width=1, color=[255//2, 255//2, 255//2]);
            game.create_line(WIDTH//2 + x * MAGNITUDEx, HEIGHT//2, WIDTH//2 + x * MAGNITUDEx, 0, width=1, color=[255//2, 255//2, 255//2]);

    # Q3
    for y in range(1,HEIGHT//MAGNITUDEy):
        for x in range(1,WIDTH//MAGNITUDEx):
            game.create_line(0, HEIGHT//2 + y * MAGNITUDEy, WIDTH//2, HEIGHT//2 + y * MAGNITUDEy, width=1, color=[255//2, 255//2, 255//2]);
            game.create_line(WIDTH//2 - x * MAGNITUDEx, HEIGHT//2+1, WIDTH//2 - x * MAGNITUDEx, HEIGHT, width=1, color=[255//2, 255//2, 255//2]);

    # Q2 
    for y in range(1,HEIGHT//MAGNITUDEy):
        for x in range(1,WIDTH//MAGNITUDEx):
            game.create_line(0, HEIGHT//2 - y * MAGNITUDEy, WIDTH//2, HEIGHT//2 - y * MAGNITUDEy, width=1, color=[255//2, 255//2, 255//2]);
            game.create_line(WIDTH//2 - x * MAGNITUDEx, HEIGHT//2, WIDTH//2 - x * MAGNITUDEx, 0, width=1, color=[255//2, 255//2, 255//2]);

    # Q4
    for y in range(1,HEIGHT//MAGNITUDEy):
        for x in range(1,WIDTH//MAGNITUDEx):
            game.create_line(WIDTH//2+1, HEIGHT//2 + y * MAGNITUDEy, WIDTH, HEIGHT//2 + y * MAGNITUDEy, width=1, color=[255//2, 255//2, 255//2]);
            game.create_line(WIDTH//2 + x * MAGNITUDEx, HEIGHT//2, WIDTH//2 + x * MAGNITUDEx, HEIGHT, width=1, color=[255//2, 255//2, 255//2]);

    if MAGNITUDEx > 3*my_font.width:
        for x in range(1,WIDTH//MAGNITUDEx):
            if MAGNITUDEx > 16:
                game.create_text(WIDTH//2 + x * MAGNITUDEx + 2, HEIGHT//2 - 1 + 14, str(x));

            for x in range(1,WIDTH//MAGNITUDEx):
                if MAGNITUDEx > 16:
                    game.create_text(WIDTH//2 + -x * MAGNITUDEx + 2, HEIGHT//2 - 1 + 14, str(-x));

            for y in range(1,HEIGHT//MAGNITUDEy):
                if MAGNITUDEy > 16:
                    game.create_text(WIDTH//2 + 3, HEIGHT//2 - y * MAGNITUDEy + 12, str(y));

            for y in range(1,HEIGHT//MAGNITUDEy):
                if MAGNITUDEy > 16:
                    game.create_text(WIDTH//2 + 3, HEIGHT//2 + y * MAGNITUDEy + 12, str(-y));

    """
    # Q2
    for y in range(HEIGHT//MAGNITUDEy):
        for x in range(WIDTH//MAGNITUDEx):
            game.create_point(WIDTH//2 + -x * MAGNITUDEx, -y * MAGNITUDEy + HEIGHT//2);

    # Q1
    for y in range(HEIGHT//MAGNITUDEy):
        for x in range(WIDTH//MAGNITUDEx):
            game.create_point(WIDTH//2 + x * MAGNITUDEx, -y * MAGNITUDEy + HEIGHT//2);
            
    # Q4
time.sleep(0.1);

    for y in range(HEIGHT//MAGNITUDEy):
        for x in range(WIDTH//MAGNITUDEx):
            game.create_point(WIDTH//2 + x * MAGNITUDEx, y * MAGNITUDEy + HEIGHT//2);

    # Q3
    for y in range(HEIGHT//MAGNITUDEy):
        for x in range(WIDTH//MAGNITUDEx):
            game.create_point(WIDTH//2 + -x * MAGNITUDEx, y * MAGNITUDEy + HEIGHT//2);
    """
    
    # Axis dots
    """
    for y in range(1,HEIGHT//MAGNITUDEy):
        game.create_point(WIDTH//2 + 1, -y * MAGNITUDEy + HEIGHT//2);

    for y in range(1,HEIGHT//MAGNITUDEy):
        game.create_point(WIDTH//2 + 1, y * MAGNITUDEy + HEIGHT//2);

    for x in range(1,HEIGHT//MAGNITUDEx):
        game.create_point(WIDTH//2 + x * MAGNITUDEx, HEIGHT//2 - 1);
        #if MAGNITUDEx > 8:
        #    game.create_text(WIDTH//2 + x * MAGNITUDEx, HEIGHT//2 - 1 + 14, str(x));

    for x in range(1,HEIGHT//MAGNITUDEx):
        game.create_point(WIDTH//2 + -x * MAGNITUDEx, HEIGHT//2 - 1);
        #if MAGNITUDEx > 8:
        #    game.create_text(WIDTH//2 + -x * MAGNITUDEx, HEIGHT//2 - 1 + 14, str(-x));
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

    return  HEIGHT - round(y * MAGNITUDEy);
    


lines:list = [];

half_width:int = WIDTH//2 / MAGNITUDEx;

for function in functions:
    points:list = [];
    x:float = 0;
    while x > half_width * -1:
        y:int = norm_to_pixel(function) - HEIGHT//2;
        if (not isinstance(y, complex) and y > -HEIGHT and y < HEIGHT*2):
            points.append((round(WIDTH//2 + x * MAGNITUDEx), y));
        x-=STEP/MAGNITUDE;

    while x < half_width:
        y:int = norm_to_pixel(function) - HEIGHT//2;
        if (not isinstance(y, complex) and y > -HEIGHT and y < HEIGHT*2):
            points.append((round(WIDTH//2 + x * MAGNITUDEx), y));
        x+=STEP/MAGNITUDE;        
        
    lines.append(points);

def key_func(e):
    return e[0];
    
#lines.sort(key=key_func, reverse=True);
    
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

print(f"The calculations took {'%.2f' % time_delta} seconds");

step_and_wait();

time_delta = (time.time() - t);

finish_text1 = game.create_text(x=3, y=16 + my_font.height + 3, text=f"Rendered in {'%.2f' % time_delta} seconds", font=my_font);
finish_text2 = game.create_text(x=3, y=15 + my_font.height + 3, text=f"Rendered in {'%.2f' % time_delta} seconds", font=my_font);
finish_text3 = game.create_text(x=2, y=16 + my_font.height + 3, text=f"Rendered in {'%.2f' % time_delta} seconds", font=my_font);
finish_text = game.create_text(x=2, y=15 + my_font.height + 3, text=f"Rendered in {'%.2f' % time_delta} seconds", color=[0,255,255], font=my_font);

print(f"The rendering took {'%.2f' % time_delta} seconds");

step_and_wait();
