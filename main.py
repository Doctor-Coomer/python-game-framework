import x11
from log import log
import time

class game_framework:     
     def __init__(self):
          self.x_win = x11.window();

     def stop(self):
          exit(0);
          
     def spawn_window(self, width:int=250, height:int=250, resizable:bool=False, title:str=""):
          self.x_win.create_win(width,height,resizable,title);

     def destroy_window(self):
          self.x_win.delete_all_win();
          
     def draw_line(self, x1:int, y1:int, x2:int, y2:int, color:tuple):
          self.x_win.draw_x11_line_with_color(x1,y1,x2,y2,color);
          
game = game_framework();

game.spawn_window(width=450, height=450, resizable=True);

