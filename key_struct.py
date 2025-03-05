class Arrow_keys:
    def __init__(self, up:bool, down:bool,
                 left:bool, right:bool):
        self.up = up;
        self.down = down;
        self.left = left;
        self.right = right;

class Mouse:
    def __init__(self, x:int, y:int,
                 left:bool, right:bool, middle:bool):
        self.x = x;
        self.y = y;
        self.left = left;
        self.right = right;
        self.middle = middle;
