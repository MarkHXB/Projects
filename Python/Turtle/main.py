"""
Summary:
    Make a simple turtle game.
    My turtle name will be theodor.

"""
#set the basic properties value to default

   

from turtle import *
setup(500,500)
Screen()
title("Turtle escape")
bgcolor("white")

theodor = Turtle()
theodor.shape("turtle")
theodor.color("brown","green")
theodor.dy = -2

ball = Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.speed(0)
ball.goto(0,200)
ball.dy = 0

wall = Turtle()
wall.shape("circle")
wall.color("black")

gravity = 0.1

import keyboard

while True:
    ball.dy -= gravity
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() < -150:
        ball.dy *= -1
    def mUp():
        theodor.forward(45)
    def mDown():
        theodor.back(45)
    def mLeft():
        theodor.left(45)
    def mRight():
        theodor.right(45)

    if keyboard.is_pressed("q"):
        break

    onkey(mUp,"Up")
    onkey(mDown,"Down")
    onkey(mLeft,"Left")
    onkey(mRight,"Right")

    listen()
    

