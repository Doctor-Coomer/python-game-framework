class Line:
    def __init__(self, index:int, x1:int, y1:int,
                 x2:int, y2:int, color:tuple,
                 width:int=2):
        self.index = index;
        self.x1 = x1;
        self.y1 = y1;
        self.x2 = x2;
        self.y2 = y2;
        self.color = color;
        self.width = width;

class FillRectangle:
    def __init__(self, index:int, x:int, y:int,
                 width:int, height:int, color:tuple):
        self.index = index;
        self.x = x;
        self.y = y;
        self.width = width;
        self.height = height;
        self.color = color;
