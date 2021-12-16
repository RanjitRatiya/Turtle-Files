from turtle import *

speed(5)
bgcolor("pink")
color("white")
pensize(10)

for i in range(6):
    left(60)
    for i in range(6):
        forward(100)
        left(60)
hideturtle()
exitonclick()
