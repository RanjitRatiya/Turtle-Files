import turtle
t = turtle.Turtle()
t.speed(1)
turtle.setup(800, 500)

t.penup()
t.goto(0, -100)
t.pendown()

t.color("red")
t.begin_fill()
t.circle(120)
t.end_fill()

t.hideturtle()
turtle.exitonclick()
