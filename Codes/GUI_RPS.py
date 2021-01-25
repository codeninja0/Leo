# Graphical User Interface RoCk PaPeR sCiSoRs
import turtle
import random
t = turtle.Turtle()
t.hideturtle()
screen = turtle.Screen()
screen.tracer(10)
t.pensize(10)
t.pu()
t.goto(-400, 200)
t.pd
t.write("Rock Paper Scissors",font=("comic sans ms", 80, "bold"))
def rocksymbol():
    t.pu()
    t.goto(-500, -50)
    t.pd()
    t.write("✊",font=("Arial", 100, "normal"))
def papersymbol():
    t.pu()
    t.goto(-50, -50)
    t.pd()
    t.write("✋",font=("Arial", 100, "normal"))
def scissorssymbol():
    t.pu()
    t.goto(300, -50)
    t.pd()
    t.write("✌️",font=("Arial", 100, "normal"))

rocksymbol()
scissorssymbol()
papersymbol()


screen.mainloop()