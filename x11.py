from Xlib import display, X, Xutil, Xatom
import threading

from log import log

class window:
    window_is_open:bool = False;
        
    def __init__(self):
        self.display = display.Display();
        self.screen = self.display.screen();
        self.root_window = self.screen.root;
        self.gc = self.root_window.create_gc(
            foreground = self.screen.black_pixel,
            background = self.screen.white_pixel,
            line_width = 2,
            line_style = X.LineSolid,
            cap_style  = X.CapRound,
            join_style = X.JoinRound
        );
        log.print("game_framework.__init__() -> window.__init__(): called");
        
    def render_loop(self):
        log.print("game_framework.spawn_window() -> window.create_win() -> window.render_loop(): called")
        while self.window_is_open == True:
            event = self.display.next_event();
            if event.type == X.Expose:
                #primary render loop
                window_width:int  = self.window.get_geometry()._data['width'];
                window_height:int = self.window.get_geometry()._data['height'];

                colormap = self.root_window.create_colormap(self.screen.root_visual, X.AllocNone);
                color = colormap.alloc_color(65535, 65535, 0);
                self.gc.change(foreground=color.pixel);
                
                self.window.line(self.gc, 0, 0,
                                 window_width,
                                 window_height,
                                 );                
                pass;
        self.display.close();
        log.print("game_framework.spawn_window() -> window.create_win() -> window.render_loop(): display closed");

    def draw_x11_line_with_color(self, x1:int, y1:int, x2:int, y2:int, color:tuple):
        return;
        
    def create_win(self, width:int, height:int, resizable:bool, title:str):
        if self.window_is_open == True:
            log.print("game_framework.spawn_window() -> window.create_win(): window already created");
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
            self.Window.set_wm_normal_hints(size_hints)
        self.window.map();
        self.window_is_open = True;
        self.display.flush();
        render_thread = threading.Thread(None, self.render_loop);
        render_thread.start();

    def delete_all_win(self):
        self.window_is_open = False;
        self.window.destroy();
        log.print("game_framework.destroy_window() -> window.delete_win(): window destroyed")
