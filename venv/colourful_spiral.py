import turtle
from random import randint

turtle.bgcolor('black')
turtle.pensize(3)
turtle.speed(0)

side_length = 5

for i in range(240):
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    turtle.colormode(255)
    turtle.pencolor((red, green, blue))
    turtle.forward(side_length)
    turtle.left(92)

    side_length +=3

turtle.exitonclick()