import turtle
import time
import threading
t=turtle.Turtle()
t.hideturtle()
t.pensize(5)
screen = turtle.Screen()
screen = turtle.Screen()
#screen.setup(800,800)
t.speed(0)
screen.tracer(0)
screen.delay(0)
side = 40
class Square:

    def __init__(self, x, y, fillcolor):
        self.x = x
        self.y = y
        self.fillcolor = fillcolor
    
    def draw(self):
        t.pu()
        t.goto(self.x,self.y)
        t.pd()
        t.color("black",self.fillcolor) 
        t.begin_fill()
        t.fd(40); t.lt(90)
        t.fd(40); t.lt(90)
        t.fd(40); t.lt(90)
        t.fd(40); t.lt(90)
        t.end_fill()

    def find(self,x,y):
        for a in range(10):
            for b in range(10):
                if squares[a][b].x == x and squares[a][b].y == y:
                    return squares[a][b]

    def findUp(self):
        return self.find(self.x, self.y+side)

    def findDown(self):
        return self.find(self.x, self.y-side)

    def findLeft(self):
        return self.find(self.x-side, self.y)

    def findRight(self):
        return self.find(self.x+side, self.y)       

    def moveUp(self):
        self.y += 40
        self.draw()
        
        screen.update()

    def moveRight(self):
        self.x += 40  
        self.draw()
        
        screen.update()

    def moveDown(self):
        self.y -= 40  
        self.draw()
        
        screen.update()

    def moveLeft(self):
        self.x -= 40  
        self.draw()
        
        screen.update()
   

    

    def goUp(self):
        self.findUp().moveDown()
        self.moveUp()
        #count()

squares = []

#screen.onkey(squares[0][0].goUp,"Up")
#squares[5][0].goUp()

for x in range(10):
    row=[]
    for y in range(10):
        row.append(Square(40*x-200,40*y-200,"skyblue"))
        row[y].draw()
    squares.append(row)
    
    #print(squares)



squares[0][0].fillcolor = "red"
squares[0][0].draw()



squares[5][0].fillcolor = "red"
squares[5][0].draw()

screen.onkey(squares[0][0].moveUp,"Up")

screen.onkey(squares[0][0].moveLeft,"Left")

screen.onkey(squares[0][0].moveDown,"Down")

screen.onkey(squares[0][0].moveRight,"Right")

def switch(x):
    squares[x][0].fillcolor,squares[x+1][0].fillcolor = squares[x+1][0].fillcolor, squares[x][0].fillcolor
    squares[x][0].draw()
    squares[x+1][0].draw()
    screen.update()

#screen.onkey(switch(0),"k")

switch(0)
time.sleep(1)
switch(0)


def move(x,y):
    #for x in range(10):
    for x in range(10):
        squares[0][0].moveUp()
    for x in range(10):
        squares[0][0].moveRight()
    for x in range(10):
        squares[0][0].moveDown()
    for x in range(10):
        squares[0][0].moveLeft()
       


screen.onscreenclick(move,1)






screen.listen()
screen.update()
screen.mainloop()
