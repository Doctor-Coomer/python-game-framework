from collections import namedtuple

import Xlib.display
from Xlib import X


disp = Xlib.display.Display()
screen = disp.screen()
root = disp.screen().root

MyGeom = namedtuple('MyGeom', 'x y height width')

w = root.create_window(0,0,500,500,1,
                       screen,
                       X.InputOutput,
                       X.CopyFromParent,
                       event_mask=X.ExposureMask | X.KeyPressMask
                       );

def get_absolute_geometry(win):
    """
    Returns the (x, y, height, width) of a window relative to the top-left
    of the screen.
    """
    geom = win.get_geometry()
    (x, y) = (geom.x, geom.y)
    while True:
        parent = win.query_tree().parent
        pgeom = parent.get_geometry()
        x += pgeom.x
        y += pgeom.y
        if parent.id == root.id:
            break
        win = parent
    return MyGeom(x, y, geom.height, geom.width)

print(get_absolute_geometry(w))
