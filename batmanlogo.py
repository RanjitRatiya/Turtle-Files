from turtle import *
bgcolor('black')
title("Batman Logo")
speed(10)
pensize(4)
begin_fill()
color('red')
left(90)
circle(50, 85)
circle(15, 110)
right(180)
circle(30, 150)
right(5)
forward(10)

right(90)
circle(-70, 140)
forward(40)
right(110)
circle(100, 30)
circle(30, 100)
left(50)
forward(50)

right(145)
forward(30)
left(55)
forward(20)
left(55)
forward(30)
right(145)
forward(50)
left(50)

circle(30, 100)
circle(100, 30)
right(110)
forward(40)
circle(-70, 140)
right(90)
forward(10)
right(5)
circle(30, 150)
left(180)
circle(15, 110)
circle(50, 85)
end_fill()
write("@ranjit_ratiya",font=("calibri 15 bold"))
hideturtle()
exitonclick()
