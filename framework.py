import signal
import sys

import x11
from log import log

class game_framework:     
     def __init__(self):
          signal.signal(signal.SIGINT, self.stop_game) #hook the Ctrl+C to a more elgant closing function
          self.x_win = x11.window(); #private instance of the window class

     def stop_game(self, sig=0, frame=0):
          log.printr("game_framework.stop_game(): starting program stop")
          self.x_win.elegant_exit();
          log.printr("game_framework.stop_game(): exited window.elegant_exit()")
          log.printr("game_framework.stop_game(): calling sys.exit()")
          sys.exit();
          
     def spawn_window(self, width:int=250, height:int=250, resizable:bool=False, title:str=""):
          self.x_win.create_win(width,height,resizable,title);

     def window_resolution(self) -> tuple:
          return self.x_win.get_window_resolution();
          
     def create_line(self, x1:int, y1:int,
                     x2:int, y2:int, color:tuple,
                     width:int=2):
          return self.x_win.create_x11_line_with_color(x1,y1,x2,y2,color,width);

     def create_fill_rectangle(self, x:int, y:int,
                          width:int, height:int, color:tuple):
          return self.x_win.create_x11_fill_rectangle_with_color(x,y,width,height,color);

