from turtle import *
setup(900,700)
speed(0)

penup()
goto(-400,250)
pendown()

#Red Rectangle
color("red")
begin_fill()
forward(800)
right(90)
forward(167)
right(90)
forward(800)
end_fill()

left(90)
penup()
forward(167)
pendown()

#Green Rectangle
color("green")
begin_fill()
left(90)
forward(800)
right(90)
forward(167)
right(90)
forward(800)
end_fill()

hideturtle()
exitonclick()