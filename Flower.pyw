from turtle import *
import turtle
color('red', 'yellow')
tut = Turtle()
screen = Screen()
screen.title("Welcom to my flower program")
tut.penup()
tut.goto(-200, 200)
tut.write('Obed Melody\nContact Me +2348102544186')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
