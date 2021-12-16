from turtle import *

speed(5)
bgcolor("pink")
color("white")
pensize(10)

for i in range(8):
    left(45)
    for i in range(8):
        forward(100)
        left(45)
hideturtle()
exitonclick()
