from turtle import *

speed(1)
setup(900, 700)

penup()
goto(-400, 250)
pendown()

# Black Rectangle
color("black")
begin_fill()
forward(267)
right(90)
forward(500)
right(90)
forward(267)
end_fill()

right(180)
forward(267)

# Yellow Rectangle
color("yellow")
begin_fill()
left(90)
forward(500)
right(90)
forward(267)
right(90)
forward(500)
end_fill()

right(180)
forward(500)

# Red Rectangle
color("red")
begin_fill()
right(90)
forward(267)
right(90)
forward(500)
right(90)
forward(267)
end_fill()

hideturtle()
exitonclick()
