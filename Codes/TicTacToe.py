# Tic Tac Toe w/ Python Turtle
import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.tracer(10)
t.speed(0)
t.pensize(10)
t.hideturtle()

screen.title("Tic Tac Toe")

symbol = "O"

noclicknomore = []

center = False
middle_left = False
middle_right = False
top_middle = False
top_left = False
top_right = False
bottom_middle = False
bottom_left = False
bottom_right = False


def switch():
    #switch
    global symbol
    if symbol == "X":
        symbol = "O"
    elif symbol == "O":
        symbol = "X"
def funcgoto(x,y,text,pos):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.write(text, font=("comic sans ms", 100, "bold"))
    print(pos)
    switch()
    print(noclicknomore)

def board():
    def drawline(x,y):
        t.penup()
        t.goto(x-100,y)
        t.pd()
        t.fd(300) #default is 0,0
    
    drawline(-100,100)
    drawline(-100,0)
    t.setheading(270)
    drawline(0,200)
    drawline(100,200)
board()
funcgoto(-300,250, "Tic Tac Toe", '')


def supermouseclick(x,y):
    global symbol
    global center
    global middle_left
    global middle_right
    global top_left
    global top_middle
    global top_right
    global bottom_middle
    global bottom_left
    global bottom_right
    if len(noclicknomore) < 9:
        if x > -95 and x < -5 and y > 5 and y < 95: #center, center
            if "center" not in noclicknomore:
                center = symbol
                print('center variable = ', center)
                funcgoto(-90,-10,symbol,'center')
                noclicknomore.append("center")
                
                
        elif x > -205 and x < -105 and y > 5 and y < 95:
            if "middle left" not in noclicknomore:
                middle_left = symbol
                print('middle left variable = ', middle_left)
                funcgoto(-190,-10,symbol,'middle left')
                noclicknomore.append("middle left")
        elif x > 5 and x < 105 and y > 5 and y < 105:
            if "middle right" not in noclicknomore:
                middle_right = symbol
                print('middle right variable = ', middle_right)
                funcgoto(10,-10,symbol,'middle right')
                noclicknomore.append("middle right")
        elif x > -205 and x < -105 and y > 105 and y < 205:
            if "top left" not in noclicknomore:
                top_left = symbol
                print('top left variable = ', top_left)
                funcgoto(-190,90,symbol,'top left')
                noclicknomore.append("top left")
        elif x > -105 and x < -5 and y > 105 and y < 205:
            if "top middle" not in noclicknomore:
                top_middle = symbol
                print('top middle variable = ', top_middle)
                funcgoto(-90,90,symbol,'top middle')
                noclicknomore.append("top middle")
        elif x > 5 and x < 105 and y > 105 and y < 205:
            if "top right" not in noclicknomore:
                top_right = symbol
                print('top right variable = ', top_right)
                funcgoto(10,90,symbol,'top right')
                noclicknomore.append("top right")
        elif x > -95 and x < -5 and y > -105 and y < -5:
            if "bottom middle" not in noclicknomore:
                bottom_middle = symbol
                print('bottom middle variable = ', bottom_middle)
                funcgoto(-90,-110,symbol,'bottom middle')
                noclicknomore.append("bottom middle")
        elif x > -205 and x < -105 and y > -105 and y < -5:
            if "bottom left" not in noclicknomore:
                bottom_left = symbol
                print('bottom left variable = ', bottom_left)
                funcgoto(-190,-110,symbol,'bottom left')
                noclicknomore.append("bottom left")
        elif x > 5 and x < 105 and y > -105 and y < -5:
            if "bottom right" not in noclicknomore:
                bottom_right = symbol
                print('bottom right variable = ', bottom_right)
                funcgoto(10,-110,symbol,'bottom right')
                noclicknomore.append("bottom right")



        if center == middle_left == middle_right == 'X':
            t.pencolor("red")
            funcgoto(-280,-300,"O go BOOM! 💥",'X wins')
        elif center == top_left == bottom_right == 'X':
            t.pencolor("red")
            funcgoto(-280,-300,"O go BOOM! 💥",'X wins')
        elif center == top_right == bottom_left == 'X':
            t.pencolor("red")
            funcgoto(-280,-300,"O go BOOM! 💥",'X wins')
        elif center == top_middle == bottom_middle == 'X':
            t.pencolor("red")
            funcgoto(-280,-300,"O go BOOM! 💥",'X wins')
        elif middle_left == top_left == bottom_left == 'X':
            t.pencolor("red")
            funcgoto(-280,-300,"O go BOOM! 💥",'X wins')
        elif middle_right == top_right == bottom_right == 'X':
            t.pencolor("red")
            funcgoto(-280,-300,"O go BOOM! 💥",'X wins')
        elif bottom_middle == bottom_left == bottom_right == 'X':
            t.pencolor("red")
            funcgoto(-280,-300,"O go BOOM! 💥",'X wins')
        elif top_middle == top_left == top_right == 'X':
            t.pencolor("red")
            funcgoto(-280,-300,"O go BOOM! 💥",'X wins')
        if center == middle_left == middle_right == 'O':
            t.pencolor("red")
            funcgoto(-280,-300,"X go BOOM! 💥",'O wins')
        elif center == top_left == bottom_right == 'O':
            t.pencolor("red")
            funcgoto(-280,-300,"X go BOOM! 💥",'O wins')
        elif center == top_right == bottom_left == 'O':
            t.pencolor("red")
            funcgoto(-280,-300,"X go BOOM! 💥",'O wins')
        elif center == top_middle == bottom_middle == 'O':
            t.pencolor("red")
            funcgoto(-280,-300,"X go BOOM! 💥",'O wins')
        elif middle_left == top_left == bottom_left == 'O':
            t.pencolor("red")
            funcgoto(-280,-300,"X go BOOM! 💥",'O wins')
        elif middle_right == top_right == bottom_right == 'O':
            t.pencolor("red")
            funcgoto(-280,-300,"X go BOOM! 💥",'O wins')
        elif bottom_middle == bottom_left == bottom_right == 'O':
            t.pencolor("red")
            funcgoto(-280,-300,"X go BOOM! 💥",'O wins')
        elif top_middle == top_left == top_right == 'O':
            t.pencolor("red")
            funcgoto(-280,-300,"X go BOOM! 💥",'O wins')
        
    elif len(noclicknomore) == 9:
            t.pencolor('light sky blue')
            funcgoto(-250,-300,"Tie 🤝 ",'tie wins')
screen.onclick(supermouseclick,1) #1 == left click on mouse  



screen.mainloop()