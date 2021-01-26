# Graphical User Interface RoCk PaPeR sCiSoRs
import turtle
import random
t = turtle.Turtle()
t.hideturtle()
screen = turtle.Screen()
screen.tracer(10)
t.pensize(10)

def write(x,y,text,size):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.write(text, font=("comic sans ms", size, "bold"))

write(-400, 200, "Rock Paper Scissors", 80)




def rocksymbol():
    write(-450, -50, "✊", 100)
def papersymbol():
    write(-50, -50, "✋", 100)
def scissorssymbol():
    write(300, -50, "✌️", 100)


rocksymbol()
papersymbol()
scissorssymbol()



screen.mainloop()