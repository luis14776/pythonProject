#Turtle Graphics

import random
import turtle
from turtle import Turtle, Screen

print('''Welcome, select your favorite shape to start drawing ;) 
            Just type: Turtle, circle, arrow, square, triangle or classic. ''')
shape = input()
screen = Screen()
koko = turtle.Turtle()
koko.speed(0)
koko.width(3)
koko.shape(shape.lower())

colors = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']

# Functions so user can control the program

def dragging(x,y):
    koko.ondrag(None)
    koko.setheading(koko.towards(x,y))
    koko.goto(x,y)
    koko.ondrag(dragging)

def star_mode():
    while True:
        for x in colors:
            koko.color(x)

def delete():
    koko.clear()

def circle():
    koko.begin_fill()   #shapes are filled with a color, while normal shapes are not filled
    koko.circle(50)
    koko.end_fill()

def normal_circle():
    koko.circle(50)

def normal_square():
    for x in range(4):
        koko.forward(100)
        koko.left(90)

def square():
    koko.begin_fill()
    for x in range(4):
        koko.forward(100)
        koko.right(90)
    koko.end_fill()

def triangle():
    koko.begin_fill()
    koko.forward(150)
    koko.right(135)
    koko.forward(150)
    koko.right(112.5)
    koko.forward(150)
    koko.end_fill()

def normal_triangle():
    koko.forward(150)
    koko.right(135)
    koko.forward(150)
    koko.right(112.5)
    koko.forward(150)

def up():
    koko.setheading(90)
    koko.forward(100)

def down():
    koko.setheading(270)
    koko.forward(100)

def left():
    koko.setheading(180)
    koko.forward(100)

def right():
    koko.setheading(0)
    koko.forward(100)

def clickleft(x,y):
    koko.color(random.choice(colors))

def space():
    koko.stamp()


turtle.listen()

turtle.onkey(star_mode, 'f')
koko.ondrag(dragging)
turtle.onkey(delete, 'd')
turtle.onkey(circle, 'c')
turtle.onkey(triangle, 't')
turtle.onkey(normal_triangle, '3')
turtle.onkey(square, 's')
turtle.onkey(normal_square, '1')
turtle.onkey(normal_circle, '2')

turtle.onscreenclick(clickleft, 1)
turtle.onkey(space, 'space')

turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

turtle.mainloop()


