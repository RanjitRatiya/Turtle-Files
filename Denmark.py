import turtle
t = turtle.Turtle()
turtle.setup(800, 500)
t.speed(1)

turtle.bgcolor("firebrick")
t.penup()
t.goto(-400, -37)
t.pendown()

# White Cross
t.color("white")
t.begin_fill()
t.forward(800)
t.left(90)
t.forward(75)
t.left(90)
t.forward(800)
t.end_fill()

t.penup()
t.goto(-100, -250)
t.pendown()

t.begin_fill()
t.forward(75)
t.right(90)
t.forward(500)
t.right(90)
t.forward(75)
t.end_fill()

t.hideturtle()
turtle.exitonclick()
