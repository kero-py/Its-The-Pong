# My first Python Pong Game
# By Ravier Gardon
# from @TokyoEdTech @freeCodeCamp.org tutorial

import turtle
import winsound
import keyboard
import time
import sys

exitGame=False
gameON=False

wn = turtle.Screen()
wn.title("It's the Pong! by R")
wn.bgcolor("black")
wn.setup(width=1000, height=600)
wn.tracer(0)

# Score
score_1 = 0
score_2 = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0.1)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=3, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-595, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0.1)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=3, stretch_len=1)
paddle_b.penup()
paddle_b.goto(590, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = .69
ball.dy = .69

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Georgia", 24))

# Function

# Game On
def startGame():
    global gameON
    gameON=True

#paddle a
def paddle_a_up():
    y = paddle_a.ycor()
    y += 60
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 60
    paddle_a.sety(y)

#paddle b
def paddle_b_up():
    y = paddle_b.ycor()
    y += 60
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 60
    paddle_b.sety(y)

# WIN
def win1():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 200)
    pen.write("Player 1 WINS!", align="center", font=("Georgia", 24))
    turtle.mainloop()

def win2():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 200)
    pen.write("Player 2 WINS!", align="center", font=("Georgia", 24))
    turtle.mainloop()
    
# quit
def quit():
    global exitGame
    exitGame=True

# Keyboard binding

#paddle a controls
wn.listen()
wn.onkeypress(paddle_a_up, "w")  
wn.onkeypress(paddle_a_down, "s")    

#paddle b controls
wn.listen()
wn.onkeypress(paddle_b_up, "Up")  
wn.onkeypress(paddle_b_down, "Down")

# quit game
keyboard.add_hotkey("q", lambda: quit())

# Main game loop

while not exitGame:
    wn.update()

    # Move the ball
    keyboard.add_hotkey("Space", lambda: startGame())
    if gameON==True:
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 345:
        ball.sety(345)
        ball.dy *= -1
        winsound.PlaySound("boing1.wav", winsound.SND_ASYNC)

    if ball.ycor() < -330:
        ball.sety(-330)
        ball.dy *= -1
        winsound.PlaySound("boing1.wav", winsound.SND_ASYNC)
    
    if ball.xcor() > 620:
        winsound.PlaySound("crowd_cheering.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 +=1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Georgia", 24))

    if ball.xcor() < -620:
        winsound.PlaySound("crowd_cheering.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 +=1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Georgia", 24))

    # Paddle and ball collisions
    if ball.xcor() > 570 and (ball.ycor() < paddle_b.ycor()  +40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(570)
        ball.dx *= -1
        winsound.PlaySound("boing1.wav", winsound.SND_ASYNC)

    if ball.xcor() < -570 and (ball.ycor() < paddle_a.ycor()  +40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-570)
        ball.dx *= -1
        winsound.PlaySound("boing1.wav", winsound.SND_ASYNC)

    if paddle_a.ycor() > 320:
        paddle_a.sety(320)

    if paddle_a.ycor() < -320:
        paddle_a.sety(-320)

    if paddle_b.ycor() > 320:
        paddle_b.sety(320)

    if paddle_b.ycor() < -320:
        paddle_b.sety(-320)

    if score_1==11:
        win1()    

    if score_2==11:
        win2()

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 150)
pen.write("Thanks for playing! :>", align="center", font=("Georgia", 24))
time.sleep(3)
sys.exit()
