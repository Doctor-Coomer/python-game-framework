class Line:
    def __init__(self, index:int, x1:int, y1:int,
                 x2:int, y2:int, color:int=[0,0,0],
                 width:int=2, style:str="solid"):
        self.index = index;
        self.x1 = x1;
        self.y1 = y1;
        self.x2 = x2;
        self.y2 = y2;
        self.color = color;
        self.width = width;
        match style:
            case "solid":
                self.style = 0; #Xlib.X.LineSolid
            case "dash":
                self.style = 1; #Xlib.X.LineOnOffDash
                
    def delete(self):
        self.index = -1; #setting the index to be negative will cause it to be ignored
        del self;
        
class Rectangle:
    def __init__(self, index:int, x:int, y:int,
                 width:int, height:int,
                 color:int=[0,0,0], filled:bool=True,
                 edge_width:int=2):
        self.index = index;
        self.x = x;
        self.y = y;
        self.width = width;
        self.height = height;
        self.color = color;
        self.filled = filled;
        self.edge_width = edge_width;
    def delete(self):
        self.index = -1;
        del self;
