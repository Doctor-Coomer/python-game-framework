#!/usr/bin/python
import time
import signal
import sys

import x11
from log import log

class game_framework:     
     def __init__(self):
          signal.signal(signal.SIGINT, self.stop_game) #hook the Ctrl+C to a more elgant closing function
          self.x_win = x11.window(); #private instance of the window class

     def stop_game(self, sig=0, frame=0):
          self.x_win.elegant_exit();
          sys.exit();
          
     def spawn_window(self, width:int=250, height:int=250, resizable:bool=False, title:str=""):
          self.x_win.create_win(width,height,resizable,title);

     def window_resolution(self) -> tuple:
          return self.x_win.get_window_resolution();
          
     def create_line(self, x1:int, y1:int,
                     x2:int, y2:int, color:tuple,
                     width:int):
          return self.x_win.create_x11_line_with_color(x1,y1,x2,y2,color,width);

     def create_fill_rectangle(self, x:int, y:int,
                          width:int, height:int, color:tuple):
          return self.x_win.create_x11_fill_rectangle_with_color(x,y,width,height,color);

game = game_framework(); #create a game instance

width = 450
height = 450

#sprites are rendered in order of declaration
#rendered first
l = game.create_line(x1=0, y1=0, x2=width, y2=height, color=(0,0,0), width=60);

l2 = game.create_line(x1=0, y1=height, x2=width, y2=0, color=(0,255,0), width=60);

#Creates window
game.spawn_window(width=width, height=height, resizable=True);

#game logic loop
i:int = 2;
while True:
     l.x2 = game.window_resolution()[0]
     l.y2 = game.window_resolution()[1]
     l.width = i%50+2;
     i+=1;
     time.sleep(0.025)
