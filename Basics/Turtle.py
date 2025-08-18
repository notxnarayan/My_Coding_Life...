from turtle import *
import math

t = Turtle()
last_pos = [None, None]
class Tree:
    def __init__(self, x, y):
        treet = Turtle()
        treet.home()
        treet.fillcolor("green")
        treet.begin_fill()
        treet.goto(x - 5, y)
        treet.goto(x +10, y)
        treet.goto(x +10, y+20)
        treet.goto(x -5, y+20)
        treet.goto(x-5, y)
        treet.end_fill()

def distance(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)

def buttonclick(x,y):
    if x > minx < maxx and y > miny< maxy:
        print("Button Clicked")
        screen.clear()
        create_axe()

        def follow_mouse_motion(event):
            # Convert tkinter (canvas) coordinates to turtle coordinates
            x = event.x - screen.window_width() // 2
            y = screen.window_height() // 2 - event.y
            if (x, y) != tuple(last_pos):
                t.goto(x, y)
                last_pos[0], last_pos[1] = x, y

        # Get the tkinter canvas and bind motion event
        canvas = screen.getcanvas()
        Tree(0, 0)
        canvas.bind("<Motion>", follow_mouse_motion)

    else:
        print("Button not clicked")




def create_axe():
    s = Shape("compound")
    poly1 = ((0,0), (0,20), (10,20), (10,0))
    s.addcomponent(poly1, "red", "blue")
    poly2 = ((10,20), (-30, 20), (-30,30), (10,30))
    s.addcomponent(poly2, "red", "blue")
    register_shape("myshape", s)
    t.shape("myshape")

screen = Screen()
startbtn = [(100,0) , (100,30), (-100,30), (-100,0), (0,0)]
maxx = 100
maxy = 30
minx = -100
miny = 0
t.begin_fill()
for i in startbtn:
    t.goto(i)
t.end_fill()
t.penup()
t.bk(70)
t.pencolor("white")
t.write("Start Game", font=("Arial", 24, "bold"))

screen.listen()
screen.onscreenclick(buttonclick)

screen.mainloop()