import signal
import sys

import x11
from log import log

class game_framework:     
     def __init__(self):
          signal.signal(signal.SIGINT, self.stop_game) #hook Ctrl+C to a more elgant closing function
          self.x_win = x11.window(); #private instance of the window class
          
     def stop_game(self, sig=0, frame=0) -> None:
          log.printr("game_framework.stop_game(): starting program stop")
          self.x_win.elegant_exit();
          log.printr("game_framework.stop_game(): exited window.elegant_exit()")
          log.printr("game_framework.stop_game(): calling sys.exit()")
          sys.exit();
          
     def spawn_window(self, width:int=250, height:int=250, resizable:bool=False, title:str="") -> None:
          self.x_win.create_win(width,height,resizable,title);
          
     def get_window_resolution(self) -> tuple:
          return self.x_win.get_window_resolution();

     def get_window_fps(self) -> float:
          return self.x_win.get_window_fps();
     
     def is_key_down(self, key:str) -> bool:
          return self.x_win.is_x11_key_down(ord(key));

     def get_arrow_keys(self):
          return self.x_win.get_x11_arrow_keys_down();
     
     def create_line(self, x1:int, y1:int,
                     x2:int, y2:int, color:int=[0,0,0],
                     width:int=2, style:str="solid"):
          return self.x_win.create_x11_line_with_color(x1,y1,x2,y2,color,width,style);
     
     def create_rectangle(self, x:int, y:int,
                          width:int, height:int, color:int=[0,0,0], filled:bool=True, edge_width:int=2):
          return self.x_win.create_x11_rectangle_with_color(x,y,width,height,color,filled,edge_width);

     def create_text(self, x:int, y:int,
                     text:str, color:int=[0,0,0]):
          return self.x_win.create_x11_text_with_color(x,y,text,color);
