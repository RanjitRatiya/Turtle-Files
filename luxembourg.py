from turtle import *
speed(1)
setup(800, 500)

goto(-400, 250)
color("red")
begin_fill()
forward(800)
right(90)
forward(167)
right(90)
forward(800)
end_fill()

left(90)
forward(167)

color("dodgerblue")
begin_fill()
forward(167)
left(90)
forward(800)
left(90)
forward(167)
end_fill()

hideturtle()
exitonclick()
