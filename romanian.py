from turtle import *
speed(1)
setup(900, 700)

penup()
goto(-400, 250)
pendown()

# blue Rectangle
color("blue")
begin_fill()
forward(267)
right(90)
forward(500)
right(90)
forward(267)
end_fill()

right(180)
forward(267)

# yellow Rectangle
color("yellow")
begin_fill()
left(90)
forward(500)
right(90)
forward(267)
right(90)
forward(500)
end_fill()

left(90)

# red rectangle
color("red")
begin_fill()
forward(267)
left(90)
forward(500)
left(90)
forward(267)
end_fill()

hideturtle()
exitonclick()
