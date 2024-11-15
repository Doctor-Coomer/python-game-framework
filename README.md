# python-game-framework
The game framework with no name. Using primarily the X11 protocol for the window, rendering, and input detection. Having Xorg doing some of the processing instead of the python interpreter should theoretically use less system resources, in comparison to doing software rendering with python alone.

# Dependencies
`Xorg/XWayland python3 python-xlib`

# Examples
Primary introduction:  
```python
#import the library
import framework

#create a framework object
game = framework.game_framework()

#create a window with a width and height of 500 pixels
game.spawn_window(width=500, height=500)

#draw a line from opposite corners of the window
my_line = game.create_line(x1=0, y1=0, x2=500, y2=500)
```
  
Tid bits:  
```python
#change attributes of the line after declaration
my_line.width = 15

#check if a key is being pressed
#with their respective ascii character
while True:
  if game.is_key_down("a") == True:
    print("the \'a\' key is being pressed.")
```
