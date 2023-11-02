import turtle
turtle.color('green')
turtle.width(3)

turtle.penup()
turtle.goto(150,-150)
turtle.pendown()

for i in range(4):
    turtle.left(90)
    turtle.forward(300)
    
turtle.exitonclick()