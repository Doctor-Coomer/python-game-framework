from Xlib import display, X, XK, Xutil, Xatom, ext
import threading
import time
import math
import subprocess
import pprint
from collections import namedtuple

import sprites
import key_struct

from log import log

class window:
    window_is_open:bool = False;

    window_target_fps:float = 0;
    window_fps:float = -1;
    
    window_width:int = 0;
    window_height:int = 0;

    window_x:int = 0;
    window_y:int = 0;

    window_bg:int = [255, 255, 255]

    draw_step_mode:bool = False;
    draw_step_ready:bool = False;

    is_drawing_frame:bool = False;
    
    cursor_x:int = 0;
    cursor_y:int = 0;
    mouse_left:bool = False;
    mouse_middle:bool = False;
    mouse_right:bool = False;
    
    stop_render_loop:bool = True;

    gc_tmp = None;
    pixmap_tmp = None;

    sprites_array = [];

    keys = [];
    
    def __init__(self):
        log.printg("game_framework.__init__() -> window.__init__(): called");
        self.display = display.Display();
        self.screen = self.display.screen();
        self.root_window = self.screen.root;
        self.keys = self.display.query_keymap();
        self.default_font = (self.display.open_font("fixed"));
        self.window_target_fps = 144#float(subprocess.check_output("xrandr | grep primary -A 1 | grep \"\\*\" | awk {\'print $2\'} | grep -Eo \'[0-9.0-9]+\'", shell=True, text=True).replace("\n", ''));
        
    def create_win(self, width:int=250, height:int=250, resizable:bool=False, title:str="", color:int=[255, 255, 255], step:bool=False):
        if self.window_is_open == True:
            log.printy("game_framework.spawn_window() -> window.create_win(): window already created");
            return;
        self.window = self.root_window.create_window(0,0,width,height,1,
                                                     self.screen.root_depth,
                                                     X.InputOutput,
                                                     X.CopyFromParent,
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
        self.window_bg = color;
        self.window.map();
        self.draw_step_mode = step;
        self.window_is_open = True;
        self.stop_render_loop = False;
        self.display.flush();
        self.render_thread = threading.Thread(None, self.render_loop);
        self.render_thread.start();
        return;

    def step_win(self):
        if self.draw_step_mode == True:
            self.is_drawing_frame = True;
            self.draw_step_ready = True;
        
    def render_loop(self):
        log.printg("game_framework.spawn_window() -> window.create_win() -> window.render_loop(): entered")
        fps_count:int = 0
        t1 = time.time()
        while True:
            if self.stop_render_loop == True:
                break;
            
            #primary render loop

            fps_count += 1

            """
            if fps_count == 60:
                fps_count = 0
                t1 = t2
                t2 = time.time()
                t_difference = t2 - t1
                print(t_difference)
            """
            
            t2 = time.time()
            if t2 - t1 >= 1:
                #log.printg(fps_count)
                self.window_fps = fps_count
                fps_count = 0
                #print(t2-t1)
                t1 = time.time()
                
            self.keys = self.display.query_keymap(); #refresh the key map on the window thread

            self.window_width  = self.window.get_geometry()._data['width'];
            self.window_height = self.window.get_geometry()._data['height'];

            org_win = self.window
            geom = org_win.get_geometry()
            (tmp_window_x, tmp_window_y) = (geom.x, geom.y)
            (self.window_x, self.window_y) = (geom.x, geom.y)
            while True:
                parent = org_win.query_tree().parent 
                pgeom = parent.get_geometry()
                tmp_window_x += pgeom.x
                tmp_window_y += pgeom.y
                if parent.id == self.root_window.id:
                    break
                org_win = parent

            self.window_x = tmp_window_x
            self.window_y = tmp_window_y
                
            self.cursor_x = self.root_window.query_pointer().root_x - self.window_x
            self.cursor_y = self.root_window.query_pointer().root_y - self.window_y

            self.mouse_left   = (self.root_window.query_pointer().mask & 256  != 0)
            self.mouse_middle = (self.root_window.query_pointer().mask & 512  != 0)
            self.mouse_right  = (self.root_window.query_pointer().mask & 1024 != 0)

            if self.draw_step_mode == False or self.draw_step_ready == True:
                #allocate the graphics context and pixmap
                pixmap = self.window.create_pixmap(self.window_width, self.window_height, self.screen.root_depth)
                gc = pixmap.create_gc(
                    foreground = self.screen.black_pixel,
                    background = self.screen.white_pixel,
                    line_width = 2,
                    line_style = X.LineSolid,
                    cap_style  = X.CapButt,
                    join_style = X.JoinMiter,
                    font = self.default_font
                );

                #print(f"\n\n\n\n\n\n\n\n{gc.query()}\n\n\n\n\n\n\n\n")
    
                #draw background
                self.change_gc_color(gc, self.window_bg);
                pixmap.fill_rectangle(gc,0,0,self.window_width,self.window_height);
            
                #draw the sprites
                i:int = 0;
                while i < len(self.sprites_array):
                    self.is_drawing_frame = True;

                    sprite = self.sprites_array[i];

                    if sprite.index == -1:
                        self.sprites_array.remove(sprite);
                        continue;
                        
                    self.change_gc_color(gc, sprite.color);

                    match type(sprite):
                        case sprites.Line:
                            if sprite.x1 > 32767 or sprite.x1 < -32767 or sprite.y1 > 32767 or sprite.y1 < -32767 or sprite.x2 > 32767 or sprite.x2 < -32767 or sprite.y2 > 32767 or sprite.y2 < -32767:
                                continue;
                            gc.change(line_width=sprite.width,
                                      line_style=sprite.style);
                            pixmap.line(gc,
                                        sprite.x1, sprite.y1,
                                        sprite.x2, sprite.y2,
                                        );                    
                        case sprites.Rectangle:
                            if sprite.filled == False:
                                gc.change(line_width=sprite.edge_width,
                                          line_style=X.LineSolid);
                                pixmap.rectangle(gc,
                                                 sprite.x, sprite.y,
                                                 sprite.width, sprite.height
                                                 );
                            elif sprite.filled == True:
                                pixmap.fill_rectangle(gc,
                                                      sprite.x, sprite.y,
                                                      sprite.width, sprite.height
                                                      );
                        case sprites.Text:
                            if sprite.x > 32767 or sprite.x < -32767 or sprite.y > 32767 or sprite.y < -32767:
                                continue;
                            try:
                                gc.change(font=sprite.font.xfont);
                            except:
                                gc.change(font=self.default_font);
                            pixmap.draw_text(gc,
                                             sprite.x, sprite.y,
                                             sprite.text
                                             );
                        case sprites.Circle:
                            if sprite.filled == True:
                                pixmap.fill_arc(gc, sprite.x, sprite.y,
                                                sprite.width, sprite.height,
                                                0, 365*65);
                            elif sprite.filled == False:
                                pixmap.arc(gc, sprite.x, sprite.y,
                                           sprite.width, sprite.height,
                                           0, 365*65);
                        case sprites.Point:
                            if sprite.x > 32767 or sprite.x < -32767 or sprite.y > 32767 or sprite.y < -32767:
                                continue;
                            pixmap.point(gc, sprite.x, sprite.y);
                    i+=1;
                #swap the pixmap buffer to the window graphics 
                self.gc_tmp = gc;
                self.pixmap_tmp = pixmap;
                self.window.copy_area(gc, pixmap, 0, 0, self.window_width, self.window_height, 0, 0);
                #free the graphics context and pixmap

                if self.draw_step_mode == False:
                    gc.free();
                    pixmap.free();
                
                if self.draw_step_mode == True:
                    self.draw_step_ready = False;
                #self.display.flush();
                """
                if self.draw_step == True and self.draw_step_ready == True or self.draw_step_count > 0:
                self.draw_step_ready = False;
                self.draw_step_count -= 1;
                if self.draw_step_count > 100:
                self.draw_step_count = 99
                """
            self.is_drawing_frame = False;

            if self.gc_tmp != None and self.pixmap_tmp != None:
                self.window.copy_area(self.gc_tmp, self.pixmap_tmp, 0, 0, self.window_width, self.window_height, 0, 0);
            time.sleep(1/self.window_target_fps);
            
        log.printg("game_framework.spawn_window() -> window.create_win() -> window.render_loop(): exited");
        return;

    def is_x11_key_down(self, key:int) -> bool:
        keycodemap = self.display.keysym_to_keycodes(key);
        keycode = list(keycodemap)[0][0]
        return ((self.keys[keycode//8]) & (1 << (keycode % 8)) != 0);

    def get_x11_arrow_keys_down(self):
        return key_struct.Arrow_keys(
            (self.keys[13] & 128 != 0), #up
            (self.keys[14] & 16  != 0), #down
            (self.keys[14] & 2   != 0), #left
            (self.keys[14] & 4   != 0)  #right
        );

    def get_pointer(self):
        return key_struct.Mouse(self.cursor_x, self.cursor_y, self.mouse_left, self.mouse_right, self.mouse_middle)
        
    def create_x11_line_with_color(self, x1:int, y1:int, x2:int, y2:int, color:int=[0,0,0], width:int=2, style:str="solid"):
        line:sprites.Line = sprites.Line(len(self.sprites_array), x1, y1, x2, y2, color, width, style);
        self.sprites_array.append(line);
        return line;

    def create_x11_rectangle_with_color(self, x:int, y:int, width:int, height:int, color:int=[0,0,0], filled:bool=True, edge_width:int=2):
        rectangle:sprites.Rectangle = sprites.Rectangle(len(self.sprites_array), x, y, width, height, color, filled, edge_width);
        self.sprites_array.append(rectangle);
        return rectangle;
    
    def create_x11_text_with_color(self, x:int, y:int, text:str, color:int=[0,0,0], font=None):
        if font is None:
            text:sprites.Text = sprites.Text(len(self.sprites_array), x, y, text, color, self.default_font);
            self.sprites_array.append(text);
            return text;
            
        text:sprites.Text = sprites.Text(len(self.sprites_array), x, y, text, color, font);
        self.sprites_array.append(text);
        return text;

    def create_x11_font(self, name:str):
        new_xfont = self.display.open_font(name);
        if new_xfont == None:
            log.printr(f"game_framework.create_font() -> window.create_x11_font(): invalid font \"{name}\"");
            self.elegant_exit();
            exit(1);
        info = new_xfont.query().char_infos[-1];
        font:sprites.Font = sprites.Font(new_xfont, info['character_width'], info['ascent']);
        return font;
        
    def create_x11_circle_with_color(self, x:int, y:int, width:int, height:int, color:int=[0,0,0], filled:bool=True):
        circle:sprites.Circle = sprites.Circle(len(self.sprites_array), x, y, width, height, color, filled);
        self.sprites_array.append(circle);
        return circle;

    def create_x11_point_with_color(self, x:int, y:int, color:int=[0,0,0]):
        point:sprites.Point = sprites.Point(len(self.sprites_array), x, y, color);
        self.sprites_array.append(point);
        return point;
        
    def change_gc_color(self, gc, color:int=[255,255,255]):
        if color[0] > 255 or color[1] > 255 or color[2] > 255:
            log.printy("window.change_gc_color(): invalid color range");
            return;
        colormap = self.root_window.create_colormap(self.screen.root_visual, X.AllocNone);
        color = colormap.alloc_color(int((color[0]/255) * 65535),
                                     int((color[1]/255) * 65535),
                                     int((color[2]/255) * 65535));
        colormap.free();
        gc.change(foreground=color.pixel);

    def get_window_resolution(self) -> tuple:
        return (self.window_width, self.window_height);
    
    def get_window_location(self) -> tuple:
        return (self.window_x, self.window_y)

    def get_pointer_location(self) -> tuple:
        return (self.cursor_x, self.cursor_y)

    def get_font_list(self) -> list:
        return self.display.list_fonts("*", 1000);

    def get_window_fps(self) -> float:
        return self.window_fps
    
    def elegant_exit(self):
        log.printr("game_framework.stop_game() -> window.elegant_exit(): called")
        if self.stop_render_loop != True:
            self.stop_render_loop = True;
            log.printr("game_framework.stop_game() -> window.elegant_exit(): waiting for window.render_loop() to stop")
            self.render_thread.join();
            log.printr("game_framework.stop_game() -> window.elegant_exit(): window.render_loop() stopped")
        else:
            log.printy("game_framework.stop_game() -> window.elegant_exit(): window.render_loop() is probably already stopped")
        self.window.destroy();
        self.display.close();



