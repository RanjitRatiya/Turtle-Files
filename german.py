from turtle import *
import turtle
speed(0)
setup(900, 700)
# turtle.write("German Flag")

penup()
goto(-400, 250)
pendown()

# Black Rectangle
color("black")
begin_fill()
forward(800)
right(90)
forward(167)
right(90)
forward(800)
end_fill()

left(90)

# Red Rectangle
color("red")
begin_fill()
forward(167)
left(90)
forward(800)
left(90)
forward(167)
end_fill()

left(180)
penup()
forward(167)
pendown()

# Yellow Rectangle
color("yellow")
begin_fill()
forward(167)
right(90)
forward(800)
right(90)
forward(167)
end_fill()

hideturtle()
exitonclick()
