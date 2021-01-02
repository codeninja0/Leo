import turtle 
t=turtle.Turtle()
t.pensize(10)
t.shape("classic")
t.speed(0)
t.width(5)

screen = turtle.Screen()
colors=['red','dodgerblue','springgreen','blueviolet','gold','orange','black']
s=100

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

def clickright(x,y):
    t.stamp()

def space():
    t.clear()
    t.penup()
    t.goto(0.00,0.00)
    t.pendown()

screen.onkey(space, 'space')

def b():
    t.color("dodgerblue")
    t.begin_fill()
    t.end_fill()

screen.onkey(b, 'b')

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

def d5():

    t.setheading(308)
    t.fd(1.28*s)

screen.listen
screen.onkey(d5,'5')

def c():
    screen.bgcolor("black")
    
screen.onkey(c,'c')

def w():
    screen.bgcolor("white")
    
screen.onkey(w,'w')



def B():
    t.color("black")
    t.begin_fill()
    t.end_fill()
screen.onscreenclick(B, 1)
screen.onkey(B, 'B')

def r():
    t.color("red")
    t.begin_fill()
    t.end_fill()
screen.onscreenclick(r, 1)
screen.onkey(r, 'r')

def o():
    t.color("orange")
    t.begin_fill()
    t.end_fill()
screen.onscreenclick(o, 1)
screen.onkey(o, 'o')

def y():
    t.color("gold")
    t.begin_fill()
    t.end_fill()

screen.onkey(y, 'y')

def g():
    t.color("springgreen")
    t.begin_fill()
    t.end_fill()
screen.onscreenclick(g, 1)
screen.onkey(g, 'g')


def p():
    t.color("purple")
    t.begin_fill()
    t.end_fill()
screen.onscreenclick(p, 1)
screen.onkey(p, 'p')



def u():
    t.penup()
screen.onkey(u, 'u')

def d():
    t.pendown()
screen.onkey(d, 'd')

def circle():
    t.circle(100)

screen.onkey(circle, 'C')

def z():
    t.undo()
screen.onscreenclick(z, 1)
screen.onkey(z, 'z')


screen.listen()  

screen.onscreenclick(clickright, 3)

screen.onkey(up, 'Up')
screen.onkey(down, 'Down')
screen.onkey(left, 'Left')
screen.onkey(right, 'Right')

screen.mainloop()