import turtle
from random import randint

turtle.bgcolor('White')
turtle.speed(0)
turtle.pensize(3)
colors = ['cyan', 'black', 'magenta', 'orange', 'violet','blue']
num_circles = 24
radius_factor = 13

for i in range(1, num_circles):
    turtle.pencolor(colors[randint(0, len(colors) - 1)])
    turtle.circle(i * radius_factor)
    turtle.penup()
    turtle.goto(0, -i*radius_factor)
    turtle.pendown()
turtle.exitonclick()

