#RonaldRusso
import sys
from graphics import *
from random import randint
import time

win = GraphWin("My Game", 800,500)
win.setBackground("light green")
gameover = False

paddle = Rectangle(Point(350, 475), Point(450,490))
paddle.setFill("red")
paddle.draw(win)

randx = randint (0,800)
ballPts = Point(randx,0)
ball = Circle(ballPts,15)
ball.draw(win)
bally = ballPts.getY()
ballx = ballPts.getX()

message = Text(Point(50,25), "Score:")
message.setSize(25)
message.draw(win)

message2 = Text(Point(120,25), 0)
message2.setSize(25)
message2.draw(win)
score = 0

while bally < 500:
    while gameover == False:

        movement = win.checkKey()
        if movement == "a":
            paddle.move(-25,0)
        elif movement == "d":
            paddle.move(25,0)

        bally = bally + 20
        ball.move(0,20)
        time.sleep(.1)
        paddlePt = paddle.getP1()
        paddlex = paddlePt.getX()
        if ballx >= paddlex and ballx <= paddlex + 100 and bally > 495:
            message2.undraw()
            score = score + 1
            message2 = Text(Point(120,25),score)
            message2.setSize(25)
            message2.draw(win)
            if score == 15:
                gameover = True
                win.close()
                exit()

        if ballx <= paddlex and bally > 495 or ballx >= paddlex + 100 and bally > 495:
            message2.undraw()
            score = score - 1
            message2 = Text(Point(120,25),score)
            message2.setSize(25)
            message2.draw(win)

            if score == -3:
                gameover = True
                win.close()
                exit()

        if bally >= 500:
            ball.undraw()
            randx = randint(10,800)
            ballPts = Point(randx,0)
            ball = Circle(ballPts,15)
            ball.draw(win)
            ballx = ballPts.getX()
            bally = 0
