import turtle 


screen=turtle.Screen()
screen.bgcolor("whitesmoke")
t=turtle.Turtle()
t.hideturtle()
m=t.clone()
m.hideturtle()
e=t.clone()
e.hideturtle()
h=t.clone()
h.hideturtle()
t.shape("circle")
m.shape("square")
e.shape("square")
h.shape("square")
t.shapesize(3)
m.shapesize(5)
e.shapesize(4)
h.shapesize(7)
t.color("dodgerblue")
m.color("gold")
e.color("springgreen")
h.color("red")
t.speed(0)
screen.update()

t.pu()
t.goto(0,-220)
t.showturtle()
t.setheading(90)

screen.title("the coolest game you have ever seen")

for x in range(1):

def medium():
                 
    m.pu()
    m.goto(0,550)
    m.showturtle()
    m.setheading(270)
    m.fd(x*1050)

def medium2():
    
    
    m.pu()
    
    m.goto(-200,550)
    m.showturtle()

    
    
    m.setheading(270)
    m.fd(x*1050)

def medium3():
    
    m.pu()
    m.goto(300,550)
    m.showturtle()
    
    m.setheading(270)
    m.fd(x*1050)

def easy():
    
    e.pu()
    e.goto(-200,550)
    e.showturtle()
    

    e.setheading(270)
    e.fd(1050)

screen.listen()

def easy2():
    
    e.pu()
    e.goto(150,550)
    e.showturtle()
    

    e.setheading(270)
    e.fd(1050)
    
screen.listen()

def easy3():
    
    e.pu()
    e.goto(50,550)
    e.showturtle()
    

    e.setheading(270)
    e.fd(1050)

screen.listen()

def hard():
    
    h.pu()
    h.goto(0,630)
    h.showturtle()
    

    h.setheading(270)
    h.fd(1150)

screen.listen()
   
def hard2():

    h.pu()
    h.goto(200,630)
    h.showturtle()
    

    h.setheading(270)
    h.fd(1150)

screen.listen()

def hard3():

    h.pu()
    h.goto(-200,630)
    h.showturtle()
    

    h.setheading(270)
    h.fd(1150)

screen.listen()

def hit():
    print("baba")
    if t.distance(m.pos()) < 100:
       screen.clear()
       print("haha")
        
    if t.distance(e.pos()) < 100:
       t.clear()
       print("haha")
    
    if t.distance(h.pos()) < 100:
       t.clear()  
       print("haha")    

def left():
    t.setheading(180)
    t.forward(25)
    t.forward(25)
    
def right():
    t.setheading(0)
    t.forward(25)
    t.forward(25)
    
screen.onkey(left, 'Left')
screen.onkey(right, 'Right')
screen.ontimer(hit(), 1000)

medium2()
easy2()
hard3()
m.hideturtle()
m.goto(0,500)
m.showturtle()
e.hideturtle()
e.goto(0,500)
e.showturtle()
h.hideturtle()
h.goto(0,500)
h.showturtle()
medium()
easy3()
hard()
m.hideturtle()
m.goto(0,500)
m.showturtle()
e.hideturtle()
e.goto(0,500)
e.showturtle()
h.hideturtle()
h.goto(0,500)
h.showturtle()
medium2()
easy()
hard2()
m.hideturtle()
m.goto(0,500)
m.showturtle()
e.hideturtle()
e.goto(0,500)
e.showturtle()
h.hideturtle()
h.goto(0,500)
h.showturtle()
medium()
easy3()
hard()
m.hideturtle()
m.goto(0,500)
m.showturtle()
e.hideturtle()
e.goto(0,500)
e.showturtle()
h.hideturtle()
h.goto(0,500)
h.showturtle()


screen.mainloop()