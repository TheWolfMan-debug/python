import turtle
import os

turtle.color("red", "green")
turtle.goto(-50,0)

turtle.begin_fill()

for i in range(5):
    turtle.forward(100)
    turtle.right(144)

turtle.end_fill()

turtle.penup()
turtle.goto(0,-67)
turtle.pendown()
turtle.pensize(5)
turtle.circle(50)


turtle.hideturtle()
turtle.done()