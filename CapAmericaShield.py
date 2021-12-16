from turtle import *
title('Captian America Shield')
speed(0)
bgcolor("Black")
shape("circle")
goto(-30, -280)
color("red")
begin_fill()
circle(300)
end_fill()

goto(-30, -240)
color("White")
begin_fill()
circle(260)
end_fill()

goto(-30, -200)
color("red")
begin_fill()
circle(220)
end_fill()

goto(-30, -160)
color("Blue")
begin_fill()
circle(180)
end_fill()

goto(-200, 75)
begin_fill()
color('white')

for i in range(5):
    forward(340)
    right(144)
end_fill()


write("@ranjit_ratiya", font=("calibri 15 bold"))
hideturtle()
exitonclick()
