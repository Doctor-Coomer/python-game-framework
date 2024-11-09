from Xlib import display, X, Xutil, Xatom, ext
import threading
import time

import sprites

from log import log

class window:
    window_is_open:bool = False;
    window_width:int = 0;
    window_height:int = 0;

    stop_render_loop:bool = True;

    sprites_array = [];
    
    def __init__(self):
        self.display = display.Display();
        self.screen = self.display.screen();
        self.root_window = self.screen.root;
        log.printg("game_framework.__init__() -> window.__init__(): called");

    
    def create_win(self, width:int, height:int, resizable:bool, title:str):
        if self.window_is_open == True:
            log.printy("game_framework.spawn_window() -> window.create_win(): window already created");
            return;        
        self.window = self.root_window.create_window(0,0,width,height,1,
                                                     self.screen.root_depth,
                                                     X.InputOutput,
                                                     X.CopyFromParent,
                                                     background_pixel=self.screen.white_pixel,
                                                     event_mask=X.ExposureMask | X.KeyPressMask
                                                     );
        if resizable == False:
            size_hints = {
                'flags': Xutil.PMinSize | Xutil.PMaxSize,
                'min_width': width,
                'min_height': height,
                'max_width': width,
                'max_height': height
            }
            self.window.set_wm_normal_hints(size_hints);
        self.window_height = height;
        self.window_width = width;
        self.window.map();
        self.window_is_open = True;
        self.stop_render_loop = False;
        self.display.flush();
        self.render_thread = threading.Thread(None, self.render_loop);
        self.render_thread.start();
        return;
        
    def render_loop(self):
        log.printg("game_framework.spawn_window() -> window.create_win() -> window.render_loop(): entered")
        while True:
            if self.stop_render_loop == True:
                break;            
            #primary render loop

            self.window_width  = self.window.get_geometry()._data['width'];
            self.window_height = self.window.get_geometry()._data['height'];

            #allocate the graphics context and pixmap
            pixmap = self.window.create_pixmap(self.window_width, self.window_height, self.screen.root_depth)
            gc = pixmap.create_gc(
                foreground = self.screen.black_pixel,
                background = self.screen.white_pixel,
                line_width = 2,
                line_style = X.LineSolid,
                cap_style  = X.CapButt,
                join_style = X.JoinBevel
            );

            #draw background
            gc.change(foreground=self.screen.white_pixel);
            pixmap.fill_rectangle(gc,0,0,self.window_width,self.window_height);

            #draw the sprites
            for sprite in self.sprites_array:
                if sprite.index == -1:
                    self.sprites_array.remove(sprite);
                    continue;
                
                self.change_gc_color(gc,
                                     sprite.color[0],
                                     sprite.color[1],
                                     sprite.color[2]);

                if type(sprite) == sprites.Line:
                    gc.change(line_width=sprite.width);
                
                    pixmap.line(gc,
                                sprite.x1, sprite.y1,
                                sprite.x2, sprite.y2,
                                );
                elif type(sprite) == sprites.FillRectangle:
                    pixmap.fill_rectangle(gc,
                                          sprite.x, sprite.y,
                                          sprite.width, sprite.height
                                          );

            #swap the pixmap buffer to the window graphics 
            self.window.copy_area(gc, pixmap, 0, 0, self.window_width, self.window_height, 0, 0);
            time.sleep(0.0033333333333330005); #magic number (causes it to loop at roughly 300 frames per second)
            #free the graphics context and pixmap
            gc.free();
            pixmap.free();
        log.printg("game_framework.spawn_window() -> window.create_win() -> window.render_loop(): exited");
        return;
        
    def create_x11_line_with_color(self, x1:int, y1:int, x2:int, y2:int, color:tuple, width:int=2):
        line = sprites.Line(len(self.sprites_array), x1, y1, x2, y2, color, width);
        self.sprites_array.append(line);
        return line;

    def create_x11_fill_rectangle_with_color(self, x:int, y:int, width:int, height:int, color:tuple):
        fillrectangle = sprites.FillRectangle(len(self.sprites_array), x, y, width, height, color);
        self.sprites_array.append(fillrectangle);
        return fillrectangle;
        
    def change_gc_color(self, gc, red:int, green:int, blue:int):
        if red > 255 or green > 255 or blue > 255:
            log.printy("window.change_gc_color(): invalid color range");
            return;
        colormap = self.root_window.create_colormap(self.screen.root_visual, X.AllocNone);
        color = colormap.alloc_color((red//255) * 65535,
                                     (green//255) * 65535,
                                     (blue//255) * 65535);
        gc.change(foreground=color.pixel);

    def get_window_resolution(self):
        return (self.window_width, self.window_height);
        
    def elegant_exit(self):
        log.printr("game_framework.stop_game() -> window.elegant_exit(): called")
        if self.stop_render_loop != True:
            self.stop_render_loop = True;
            log.printr("game_framework.stop_game() -> window.elegant_exit(): waiting for window.render_loop() to stop")
            self.render_thread.join();
            log.printr("game_framework.stop_game() -> window.elegant_exit(): window.render_loop() stopped")
        else:
            log.printy("game_framework.stop_game() -> window.elegant_exit(): window.render_loop() is already stopped")



