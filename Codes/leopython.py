import turtle 
from turtle import Turtle, Screen

screen=Screen()
t=Turtle("square")
t.speed(-1)
t.pensize(10)
s=40

def dragging(x, y):
    
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)

def space():
    t.clear()
    t.penup()
    t.goto(0.00,0.00)
    t.pendown()

screen.onkey(space, 'space')


def background5():
    screen.bgcolor("black")
    
screen.onkey(background5,'5')

def backroundw():
    screen.bgcolor("white")

screen.onkey(backroundw, 'w')

def backroundR():
    screen.bgcolor("red")

screen.onkey(backroundR, 'R')
  


def backroundY():
    screen.bgcolor("gold")

screen.onkey(backroundY, 'Y')

def backroundG():
    screen.bgcolor("springgreen")

screen.onkey(backroundG, 'G')

def backround7():
    screen.bgcolor("dodgerblue")

screen.onkey(backround7, '7')


def up():
    t.setheading(90)
    t.forward(s)

def down():
    t.setheading(270)
    t.forward(s)

def left():
    t.setheading(180)
    t.forward(s)

def right():
    t.setheading(0)
    t.forward(s)

def d1():

    t.setheading(45)
    t.fd(1.41*s)

screen.listen
screen.onkey(d1,'1')

def d2():

    t.setheading(135)
    t.fd(1.41*s)

screen.listen
screen.onkey(d2,'2')

def d3():

    t.setheading(225)
    t.fd(1.41*s)

screen.listen
screen.onkey(d3,'3')

def d4():

    t.setheading(315)
    t.fd(1.41*s)

screen.listen
screen.onkey(d4,'4')

def Black():
    t.color("black")
    t.begin_fill()
    t.end_fill()

screen.onkey(Black, 'B')

def red():
    t.color("red")
    t.begin_fill()
    t.end_fill()

screen.onkey(red, 'r')

def orange():
    t.color("orange")
    t.begin_fill()
    t.end_fill()

screen.onkey(orange, 'o')

def yellow():
    t.color("gold")
    t.begin_fill()
    t.end_fill()

screen.onkey(yellow, 'y')

def green():
    t.color("springgreen")
    t.begin_fill()
    t.end_fill()

screen.onkey(green, 'g')

def blue():
    t.color("dodgerblue")
    t.begin_fill()
    t.end_fill()

screen.onkey(blue, 'b')

def purple():
    t.color("purple")
    t.begin_fill()
    t.end_fill()

screen.onkey(purple, 'p')

def penup():
    t.penup()

screen.onkey(penup, 'u')

def pendown():
    t.pendown()

screen.onkey(pendown, 'd')

def circle():
    t.circle(100)

screen.onkey(circle, 'c')

def z():
    t.undo()
    
screen.onscreenclick(z, 1)
screen.onkey(z, 'z')


screen.onkey(up, 'Up')
screen.onkey(down, 'Down')
screen.onkey(left, 'Left')
screen.onkey(right, 'Right')

def main():
    screen.listen()

    t.ondrag(dragging)

    screen.onclick(space, 3)

    screen.mainloop()

main()